from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os
from time import time
from time import sleep


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
'start':'1',
'limit':'15',
'convert':'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'b32eb905-c04a-4b3c-a494-3f81d89aec8f',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    #print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

df = pd.json_normalize(data['data'])
df ['timestamp'] = pd.to_datetime('now')
df

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'15',
    'convert':'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'b32eb905-c04a-4b3c-a494-3f81d89aec8f',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    df = pd.json_normalize(data['data'])
    df ['timestamp'] = pd.to_datetime('now', utc = True)
    df
    
    if not os.path.isfile(r'E:\crypto\API.csv'):
        df.to_csv(r'E:\crypto\API.csv', header = 'column_names')
    else:
        df.to_csv(r'E:\crypto\API.csv', mode = 'a', header = False )


for i in range(333):
    api_runner()
    print("API Runner completed")
    sleep(60)

#df5 = pd.read_csv(r'E:\crypto\API.csv')
#df5



