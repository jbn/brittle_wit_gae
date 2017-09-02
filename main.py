from flask import Flask, render_template, request, jsonify, redirect
from twitter_auth import twitter_auth

app = Flask(__name__)
app.register_blueprint(twitter_auth, url_prefix='/twitter_auth')


@app.route('/')
def index():
    return render_template('index.html')
