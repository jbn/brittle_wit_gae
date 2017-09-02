from flask import Blueprint, jsonify, redirect, request
from requests import request as fetch
import requests_toolbelt.adapters.appengine
from brittle_wit_core import (AppCredentials,
                              obtain_request_token,
                              extract_access_token,
                              redirect_url,
                              obtain_access_token,
                              extract_request_token)

# You need this to use requests (for humans) on GAE.
requests_toolbelt.adapters.appengine.monkeypatch()

APP_CRED = AppCredentials.load_from_env()

twitter_auth = Blueprint('twitter_auth', 'twitter_auth',
                         template_folder='templates')


@twitter_auth.route('/login', methods=['POST'])
def login():
    callback_url = "http://localhost:8080/twitter_auth/verify"
    twitter_req, headers = obtain_request_token(APP_CRED, callback_url)
    resp = fetch(twitter_req.method,
                 twitter_req.url,
                 params=twitter_req.params,
                 headers=headers)

    status, content = resp.status_code, resp.content
    oauth_token, oauth_secret = extract_request_token(status, content)
    if not oauth_token:
        return 'Could not get an oauth token from twitter', 401
    else:
        return redirect(redirect_url(oauth_token))


@twitter_auth.route('/verify', methods=['GET'])
def verify():
    oauth_token = request.args.get('oauth_token')
    oauth_verifier = request.args.get('oauth_verifier')
    if not oauth_token or not oauth_verifier:
        return 'The client request was invalid', 400

    twitter_req, headers = obtain_access_token(APP_CRED,
                                               oauth_token,
                                               oauth_verifier)

    resp = fetch(twitter_req.method,
                 twitter_req.url,
                 params=twitter_req.params,
                 headers=headers)

    d = extract_access_token(resp.status_code, resp.content)
    if not d:
        return 'Client did not authorize the app', 401
    else:
        return jsonify(d)
