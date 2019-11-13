from flask import Flask, render_template


result = [
        {
            "color": (141, 125, 83),
            "weight": 76.37,
            "name": "Clay Creek",
            "rank": 1,
            "class": "Grey"
        },
        {
            "color": (35, 22, 19),
            "weight": 23.63,
            "name": "Seal Brown",
            "rank": 2,
            "class": "Black"
        }
    ]

app = Flask(__name__,
            template_folder = 'templates')

@app.route('/')
def hello():
    return 'Hello world from Flask'

@app.route('/hello')
def hello1():
    return render_template('hello.html')

@app.route('/task4')
def task4():
	return render_template('task4.html', result = result)