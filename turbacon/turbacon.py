#import json
import os
import urllib
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, json

api_key = os.getenv('API_KEY_TURBACON', "not found")
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
))

app.config.from_envvar('TURBACON_SETTINGS', silent=True)

def query_google_kgs():
    params = {
        "query": "taylor swift",
        "limit": 1,
        "indent": True,
        "key": api_key,
    }
    url = service_url + "?" + urllib.parse.urlencode(params)
    response = json.loads(urllib.request.urlopen(url).read())
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query')
def query():
    result = query_google_kgs()
    response = app.response_class(
        response=str(result),
        status=200,
        mimetype='application/json',
    )
    return response

