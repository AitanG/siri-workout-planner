import functions_framework
import os.path
import requests

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from workout_planner.get_power_sets import get_power_sets
from workout_planner.user_data import USER_DATA


# If modifying these scopes, delete the files _____-token.json.
GOOGLE_API_SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file',
]

PUSHOVER_MESSAGE_TITLE = 'Workout'


def get_sheets_api_credentials(user_key):
    '''Get Google Sheets API OAuth 2.0 credentials.

    _____-credentials.json file is downloaded from GCP OAuth setup.

    The files _____-token.json store the user's access and refresh tokens, and are
    created automatically when the authorization flow completes for the first time.
    '''
    creds = None
    if os.path.exists(f'{user_key}-token.json'):
        creds = Credentials.from_authorized_user_file(f'{user_key}-token.json', GOOGLE_API_SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                f'{user_key}-credentials.json', GOOGLE_API_SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(f'{user_key}-token.json', 'w') as token:
            token.write(creds.to_json())

    return creds


def fetch_workout_history(user_key):
    '''Fetches previous workout history from Google Sheet as input for new workout plan.
    '''
    creds = get_sheets_api_credentials(user_key)
    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=USER_DATA[user_key]['spreadsheet_id'],
                                    range='Sheet1').execute()
        rows = result.get('values', [])
        # Ensure all rows fill 3 columns even if missing data
        for row in rows:
            while len(row) < 3:
                row.append('')

        with open(f'{user_key}-history.txt', 'w', encoding='utf-8') as f:
            f.seek(0)
            f.write('\n'.join(','.join(row) for row in rows))

    except HttpError as err:
        print(err)


def send_pushover_notification(user_key, workout_plan):
    '''Sends the user a Pushover push notification with their new workout plan.
    '''
    pushover_token = USER_DATA[user_key]['pushover_token']
    pushover_user = USER_DATA[user_key]['pushover_user']
    url = (f'https://api.pushover.net/1/messages.json?token={pushover_token}&user={pushover_user}'
           f'&title={PUSHOVER_MESSAGE_TITLE}&message={workout_plan}')
    response = requests.post(url)
    print(response.json())


def push_workout_history(user_key):
    '''Pushes updated workout history (now in local file) to Google Sheet.
    This can be edited later in Google Sheets UI to reflect any deviations from the plan.
    '''
    creds = get_sheets_api_credentials(user_key)
    service = build('sheets', 'v4', credentials=creds)
    with open(f'{user_key}-history.txt', 'r', encoding='utf-8') as f:
        txt_raw = f.read()
        values = list(map(lambda line: tuple(line.strip().split(',')),
                          txt_raw.strip().split('\n')))
        value_range_body = {
            'range': 'A1:C9999',
            'values': values,
        }
        request = service.spreadsheets().values().update(
            spreadsheetId=USER_DATA[user_key]['spreadsheet_id'],
            range='A1:C9999',
            valueInputOption='RAW',
            body=value_range_body,
        )
        response = request.execute()
    print(response)


def generate_power_sets(user_key, num_power_sets, gym):
    '''Defines high-level app functionality.
    '''
    fetch_workout_history(user_key)
    try:
        result = get_power_sets(
            user_key,
            num_power_sets,
            gym,
            input_filename=f'{user_key}-history.txt',
            output_filename=f'{user_key}-history.txt',
        )
    except Exception as e:
        send_pushover_notification(user_key, f'Error:\n\n{e}')
    else:
        send_pushover_notification(user_key, result)
        push_workout_history(user_key)


@functions_framework.http
def hello_http(request):
    '''HTTP Cloud Function.
    Args:
         request (flask.Request): The request object.
         <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
         The response text, or any set of values that can be turned into a
         Response object using `make_response`
         <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    '''
    request_args = request.args
    if not request_args or 'user_key' not in request_args:
        return 'Failure'

    user_key = request_args['user_key']
    num_power_sets = int(request_args.get('num_power_sets', 2))
    gym = request_args.get('gym', 'office').lower()

    generate_power_sets(user_key, num_power_sets, gym)

    return 'Success!'
