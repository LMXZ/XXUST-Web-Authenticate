import requests
import json
from time import sleep
import random

with open('./config.json', 'r') as file:
    config = json.load(file)
    url, data, testInterval, testIntervalRandRange = \
        config['url'], config['data'], config['testInterval'], config['testIntervalRandRange']
    assert(testIntervalRandRange <= testInterval)

with open('./headers.txt', 'r') as file:
    headersLoginTxt = file.read()

while True:
    try:
        print('testing network...')
        requests.get('https://www.baidu.com')
        print('succeed!')
        wait_time = testInterval+random.random() * testIntervalRandRange * 2 - testIntervalRandRange
        print(f'next test in {wait_time} seconds...')
        sleep(wait_time)
    except:
        while True:
            print('failed! trying to reconnect')

            try:
                # urlc = 'http://222.197.192.59:9090/zportal/loginForWeb?wlanuserip=76f0a23a9945f920822c585e0280ce87&wlanacname=c8c9622958c8e70501e9284a0abec0fc&ssid=&nasip=cbde5ddbb5eb03be513e83acf881fb36&snmpagentip=&mac=e93ae7583b4c6391b04da4be2082744d&t=wireless-v2&url=d4985c1eb88f0cfdb5825733b7731ab1291298f53526e958e8cae5e588442a03&apmac=&nasid=c8c9622958c8e70501e9284a0abec0fc&vid=0aba78f106256def&port=49427237d34089c8&nasportid=b8007b401a20ea6148051ee1abfa64598c5a0f9754dde85cdc3ef59678c89140'
                # cookie = requests.get(urlc).cookies
                # print(headersLogin)
                headersLogin = {k: v for k, v in map(lambda x: x.split(': '), headersLoginTxt.split('\n')[1:])}
                # headersLogin['Cookie'] = f'JSESSIONID={cookie.get_dict()["JSESSIONID"]}'
                resp = requests.post(url, headers=headersLogin, data=data.encode('ascii'))
                print('reconnect', json.loads(resp.content)['result'])
                break
            except:
                print('reconnect failed')
                print('***please see the document README.md, ***\n***make sure you have entered the required information appropriately.***')
            
            wait_time = 10+random.random() * 3
            print(f'retry in {wait_time} seconds...')
            sleep(wait_time)