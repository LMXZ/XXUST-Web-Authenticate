import requests
import json
from time import sleep
import random

with open('./config.json', 'r') as file:
    config = json.load(file)
    url, data = config['url'], config['data']

with open('./headers.txt', 'r') as file:
    headersLoginTxt = file.read()

while True:
    try:
        print('testing network...')
        requests.get('https://www.baidu.com')
        print('succeed!')
        wait_time = 60+random.random() * 10
        print(f'next test in {wait_time} seconds...')
        sleep(wait_time)
    except:
        while True:
            print('failed! trying to reconnect')

            headersLogin = {k: v for k, v in map(lambda x: x.split(': '), headersLoginTxt.split('\n')[1:])}

            resp = requests.post(url, headers=headersLogin, data=data.format(username='201910416135', pwd='12wyw...').encode('ascii'))
            try:
                print('reconnect', json.loads(resp.content)['result'])
                break
            except:
                print('reconnect failed')
            
            wait_time = 10+random.random() * 3
            print(f'retry in {wait_time} seconds...')
            sleep(wait_time)