from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
	return render_template('index.html')

'''@app.route('/user/', methods=['POST', 'GET'], defaults={'email': None, 'password': None})
def user(email, password):
      email = request.args.get('email')
      password = request.args.get('password')
      
      if not email or not password:
        return \
          "<p>Something went wrong</p>\n" + \
          "<a href='/'>\n" + \
			    "<button>Home</button>\n" + \
		      "</a>\n"
      
      return render_template('user.html', email=email)'''

@app.route('/login/', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		session['username'] = username
		return redirect(url_for('index'))
	return render_template('login.html')  # executed on GET


@app.route('/logout/', methods=['GET'])
def logout():
	session.pop('username')
	return redirect(url_for('index'))
