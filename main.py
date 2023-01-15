import functions_framework
import os.path
import requests

from workout_planner.get_power_sets import get_power_sets
from workout_planner.user_data import USER_DATA

import store


PUSHOVER_MESSAGE_TITLE = 'Workout'


def send_pushover_notification(user_key, workout_plan):
    '''Sends the user a Pushover push notification with their new workout plan.
    '''
    pushover_token = USER_DATA[user_key]['pushover_token']
    pushover_user = USER_DATA[user_key]['pushover_user']
    url = (f'https://api.pushover.net/1/messages.json?token={pushover_token}&user={pushover_user}'
           f'&title={PUSHOVER_MESSAGE_TITLE}&message={workout_plan}')
    response = requests.post(url)


def generate_power_sets(user_key, num_power_sets, gym):
    '''Defines high-level app functionality.
    '''
    store.get_history(user_key)
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
        store.update_history(user_key)


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


if __name__ == '__main__':
    print(store.get_history(TEST_USER))
