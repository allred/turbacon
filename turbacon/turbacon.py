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

def query_google_kgs(q=None):
    if q is None:
        return {}
    params = {
        "query": q,
        "limit": 10,
        "indent": False,
        "key": api_key,
    }
    url = service_url + "?" + urllib.parse.urlencode(params)
    response = json.loads(urllib.request.urlopen(url).read())
    return response

@app.route('/')
def index():
    q = request.args.get('q')
    result = query_google_kgs(q)
    return render_template('index.html', results=result, q=q)
    #return render_template('index.html', results=request.args)

@app.route('/query')
def query(term=None, limit=None):
    result = query_google_kgs()
    response = app.response_class(
        response=str(result),
        status=200,
        mimetype='application/json',
    )
    return response

