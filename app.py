import requests
import json 
from django.http import HttpResponse

key = '1SXC5NCVKRJPOEG6'
ticker = 'AAPL'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)
response = requests.get(url)
print(response.json()) 
HttpResponse(response.json())