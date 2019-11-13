from flask import Flask, render_template
from flask_wtf import FlaskForm

multimedia_formats = {
"audio": ["flac", "m4a", "mp3", "wav", "ogg", "aiff"],
"image": ["jpeg", "gif", "tiff", "png", "svg"]
}

app = Flask(__name__, template_folder="templates")


@app.route('/')
def test():
	return render_template('index.html', my_data = multimedia_formats)