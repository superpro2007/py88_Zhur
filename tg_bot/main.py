import config
import requests

# https://api.telegram.org/bot{API_KEY}/{METHOD}

offset = 0
limit = 1
timeout = 20

while True:
    # api-endpoint
    URL = f"https://api.telegram.org/bot{config.TG_BOT_TOKEN}/getUpdates"

    params = {
        'offset': offset,
        'limit': limit,
        'timeout': timeout
    }

    # sending get request and saving the response as response object
    response = requests.get(url=URL, params=params)

    # extracting data in json format
    data = response.json()
    result = data['result']
    if result:
        element = result[0]
        update_id = element['update_id']
        offset = update_id + 1
        message = element['message']
        text = message['text']

        # printing the output
        print(text)

# {
#     'ok': True,
#     'result': [
#         {
#             'update_id': 85451127,
#             'message': {'message_id': 1, 'from': {'id': 89679113, 'is_bot': False, 'first_name': 'Yako', 'last_name': 'Tako', 'username': 'Vex_machine', 'language_code': 'en'}, 'chat': {'id': 89679113, 'first_name': 'Yako', 'last_name': 'Tako', 'username': 'Vex_machine', 'type': 'private'}, 'date': 1685644004, 'text': '/start', 'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]}
#         }
#     ]
# }
