import requests
import json 
key = '1SXC5NCVKRJPOEG6'
ticker = 'AAPL'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)
response = requests.get(url)
print(response.json()) 
HttpResponse('<pre>' + response.json() + '</pre>')