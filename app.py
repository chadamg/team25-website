from flask import Flask, render_template, request
from random import choice

web_site = Flask(__name__)

@web.site.route('/')
def index():
    return render_template('index.html')

@web_site.route('/user', methods=['POST', 'GET'])
def login():

    if request.method == 'GET':

        return("<pUser: " + request.args.get('username') + "</p>")

web_site.run(host='0.0.0.0', port=8080)


