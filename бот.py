import requests
from time import sleep
url = "https://api.telegram.org/bot637253940:AAGGm70grKmfq6U8jLbm2JTFIZbiuLx5YAc/"



def get_updates_json(request):
    params = {'timeout': 100, 'offset' : None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()



def last_update(data):
    result = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id' : chat, 'text' : text}
    response = requests.post(url + 'sendMessage' , data=params)
    return response

def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
            update_id +=1
        sleep(1)

if__name__=='__main__':
    main()
