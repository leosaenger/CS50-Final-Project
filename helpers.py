# Strava modules
from __future__ import print_function
import time
import urllib3
from pprint import pprint
try:
    from urllib.parse import urlparse
except ImportError:
    # Python 2
    from urlparse import urlparse

# Flask session control tools
from flask import redirect, render_template, request, session
from functools import wraps

# Polyline encoding/decoding: https://pypi.org/project/polyline/
import polyline

# As per: https://pythonhosted.org/stravalib
from stravalib import Client

# Sets our key
key = '2e817e5134aa77e0d28836b55d7519ecc1a1d3d4'


def get_segments(lowerlat, lowerlong, upperlat, upperlong):
    '''Accepts lower and upper bounds for an area, and returns a list of polylines for nearby segments'''
    # EXAMPLE: get_segments(42.377003,-71.116661,42.387596,-71.099495)

    client = Client()
    client = Client(access_token=key)
    data = client.explore_segments([lowerlat,lowerlong,upperlat,upperlong], activity_type='running')

    # Iterates over the object returned, taking out polylines
    polylines = []
    try:
        for n in data['segments']:
            polylines.append(n['points'])
    except KeyError:
        print("No segments in area!")
    return polylines

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def refresh_token():
    info = {grant_type: refresh_token,
            refresh_token: "ed64949d3614e9a0574ecba44d5514de593c2c0b"}
    token = requests.post('https://www.strava.com/oauth/token', info=info)
    return(token)
