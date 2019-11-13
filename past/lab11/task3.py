from flask import Flask, render_template
app = Flask(__name__,
			template_folder = 'templates')

@app.route('/')
def hello():
	return 'Hello world from Flask'

@app.route('/hello')
def hello1():
	return render_template('hello.html')