from flask import Flask
import requests

app = Flask(__name__)

API_URL = 'https://financialmodelingprep.com/api/v3/quote-short/{ticker}'

def fetch_price(ticker):
    data = requests.get(API_URL.format(ticker=ticker.upper()), params={'apikey': 'demo'}).json()
    return data[0]['price']

# App endpoint will be
# http://localhost:5000/stock/AAPL

@app.route('/stock/<ticker>')
def stock(ticker):
    price = fetch_price(ticker)
    return f'The price of {ticker} is {price}'

@app.route('/')
def home_page():
    return 'Try /stock/AAPL'