import json
import jwt
import os
import requests
import time

from workout_planner.user_data import USER_DATA


TOKEN_REQUEST_URL_V3 = 'https://www.googleapis.com/oauth2/v3/token'
TOKEN_REQUEST_URL_V4 = 'https://www.googleapis.com/oauth2/v4/token'

SCOPE = (
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.appdata',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive.metadata',
    'https://www.googleapis.com/auth/drive.metadata.readonly',
    'https://www.googleapis.com/auth/drive.photos.readonly',
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/drive.scripts'
)


CSV_EXPORT_URL = 'https://www.googleapis.com/drive/v3/files/{id}/export'
SHEET_UPDATE_URL = 'https://sheets.googleapis.com/v4/spreadsheets/{id}:batchUpdate'


def update_history(user_key):
    '''Updates the spreadsheet with history from _____-history.txt.
    '''
    with open(f'{user_key}-history.txt', 'r', encoding='utf-8') as f:
        txt_raw = f.read()
        values = list(map(lambda line: {
            'values': list(__string_to_cell_val(s) for s in line.strip().split(',')),
        }, txt_raw.strip().split('\n')))

    update_cells_request = {
        'updateCells': {
            'rows': values,
            'fields': 'userEnteredValue',
            'start': {
                'sheetId': 0,
                'rowIndex': 0,
                'columnIndex': 0,
            }
        }
    }
    body = {
        'requests': [update_cells_request]
    }
    access_token = __get_access_token(user_key, TOKEN_REQUEST_URL_V4)
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Accept': 'application/json',
    }

    response = requests.post(SHEET_UPDATE_URL.format(id=USER_DATA[user_key]['google_drive_file_id']), data=json.dumps(body), headers=headers)
    return response


def get_history(user_key):
    '''Gets the full CSV contents of the spreadsheet.
    '''
    access_token = __get_access_token(user_key, TOKEN_REQUEST_URL_V3)
    params = {
        'mimeType': 'text/csv',
        'key': USER_DATA[user_key]['google_drive_api_key'],
    }
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Accept': 'application/json',
    }

    response = requests.get(CSV_EXPORT_URL.format(id=USER_DATA[user_key]['google_drive_file_id']), params=params, headers=headers)
    response = '\n'.join(line for line in response.text.split('\r\n'))

    with open(f'{user_key}-history.txt', 'w', encoding='utf-8') as f:
        f.seek(0)
        f.write(response)


def __string_to_cell_val(string):
    return {
        'userEnteredValue': {
            'stringValue': string,
        }
    }


def __get_access_token(user_key, token_request_url):
    '''Gets the RS256-encoded JWT for accessing the Google Drive API.
    '''
    with open(f'{user_key}-workout-key.json', 'r') as f:
        private_key = json.loads(f.read())

    kid = private_key['private_key']
    iss = private_key['client_email']
    sub = private_key['client_email']
    iat = time.time()
    exp = iat + 3600

    payload = {
        'aud': TOKEN_REQUEST_URL_V3,
        'iat': iat,
        'exp': exp,
        'iss': iss,
        'sub': sub,
        'scope': ' '.join(SCOPE)
    }

    jwt_encoded = jwt.encode(payload, kid, algorithm='RS256')

    response = requests.post(token_request_url, data={
        'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
        'assertion': jwt_encoded,
    })

    return response.json()['access_token']
