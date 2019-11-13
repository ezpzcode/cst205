from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

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

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)

class artist_list(FlaskForm):
    artist_name = StringField('Artist Name', validators=[DataRequired()])
    submit = SubmitField('Click')

artistlist = []

def store_artist(my_artist):
    artistlist.append(dict(
        artistname = my_artist,
        date = datetime.today()
    ))

@app.route('/artist', methods=['GET','POST'])
def index():
    form = artist_list()
    if form.validate_on_submit():
        store_artist(form.artist_name.data)
        print(artistlist)
        return redirect('/al')
    return render_template('index.html', form=form)

@app.route('/al')
def al():
    return render_template('al.html', artistlist=artistlist)

@app.route('/')
def hello():
    return 'Hello world from Flask'

@app.route('/hello')
def hello1():
    return render_template('hello.html')

@app.route('/task4')
def task4():
    return render_template('task4.html', result = result)