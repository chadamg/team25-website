from flask import Flask, render_template, request

web_site = Flask(__name__)

@web_site.route('/')
def index():
	return render_template('index.html')

@web_site.route('/user/', methods=['POST', 'GET'], defaults={'email':None, 'password':None})
@web_site.route('/user/<email>')
@web_site.route('/user/<password>')
def login(email, password):
      if not email and not password:
        email = request.args.get('email')
        password = request.args.get('password')
      
      if not email or not password:
        return "Something went wrong"
      
      return "You are signed in as " + email

#only used for repl.it:
#web_site.run(host='0.0.0.0', port=8080)