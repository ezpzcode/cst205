from flask import Flask
# create an instance of the Flask class
app = Flask(__name__)
# route() decorator binds a function to a URL
@app.route('/hello')
def hello():
	return 'Hello world from Flask'