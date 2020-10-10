from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return "Welcome to the index page."

@app.route('/hello/')
def hello():
	return "Hello World!"

@app.route('/hello/<username>')
def greet(username):
	return 'Hi there, {}'.format(username)

if __name__ == '__main__':
	app.run()