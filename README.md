# flask-stock-app

Basic stock price app with Flask. This app desmonstrates making simple api requests for current stock prices of some specific stocks.
It makes use of Jinja2 templates with partials and macros. 

# Note: 
The app makes calls to the [financialmodellingprep](https://financialmodelingprep.com/) api, to 
get pricing for all the stocks featured in the app, you will need to get your own API KEY. A free tier is available 
for that on above website.

## Run locally:
```clone``` or ```fork``` the repository e.g.

```git clone https://github.com/Tig10/flask-stock-app.git```

```$ cd flask-stock-app```

```$ pip install -r requirements.txt```

```$ FLASK_APP=app FLASK_ENV=development flask run```
