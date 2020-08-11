import requests
from datetime import datetime


stocks = [
    'AAPL',
    # 'MSFT',
    # 'AMZN',
    # 'GOOGL',
]

# BASEURL = 'https://api.twelvedata.com/price'

BASEURL = 'https://api.twelvedata.com/time_series'
APIKEY = 'e99d02e0e26144ada92a05e4ca5fd534'

# Current date : yyyy-mm-dd
date = str(datetime.date(datetime.now()))

# Speech Starting/Ending Time (est) : hh:mm:00
start_time = '11:00:00'
end_time = '11:01:00'

start_date = date + " " + start_time
end_date = date + " " + end_time

# Options: 1min, 5min, 15min, 30min, 45min, 1h, 2h, 4h, 1day, 1week, 1month
interval = '1min'


for stock in stocks:

    # response = requests.get('{}?symbol={}&apikey={}'.format(BASEURL, stock, APIKEY))
    response = requests.get('{}?symbol={}&interval={}&start_date={}&end_date={}&apikey={}'.format(BASEURL, stock, interval, start_date, end_date, APIKEY))
    data = response.json()['values']
    print(stock)
    for value in data:
        print('Time' , value['datetime'])
        print('Open', value['open'])
        print('Close', value['close'])
        print('High', value['high'])
        print('Low', value['low'])

        print()
       
    