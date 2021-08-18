#!/usr/local/env python3.9

import json
import configparser
from flask import Blueprint, Flask, render_template, redirect, url_for, request, jsonify, abort
from flask_login import LoginManager, login_user, logout_user, UserMixin, current_user, login_required
from flask import render_template_string, redirect
from functools import wraps

config = configparser.ConfigParser()
config.read('config/config.ini')

app = Flask(__name__)
app.secret_key = config['app']['secret_key']

def is_validkey(key):
  with open('api.keys', 'r') as f:
    keys = json.load(f)
  if key in keys:
    return True
  return False

def require_appkey(view_function):
  @wraps(view_function)
  def decorated_function(*args, **kwargs):
    if request.headers.get('x-api-key') and is_validkey(request.headers.get('x-api-key')):
      return view_function(*args, **kwargs)
    else:
      abort(401)
  return decorated_function

@app.route('/', methods=['GET'])
def index():
  return {"msg": "No auth needed"}

@app.route('/auth/', methods=['POST', 'GET'])
@require_appkey
def auth():
  if request.method == 'GET':
    return {"msg": "API key Valid"}
  return {"msg": "API key Not Valid"}

if __name__ == '__main__':
  app.run(debug=True)
