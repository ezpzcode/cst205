"""
Name : YE LIN JOH
Date : 11/12/2019
Course : CST 205
Description : The code generates a homepage showing refreshed, three different random images from the saved images 
	and descriptive pages for each of the images. It shows the descriptive page when clicking on the titles,
	and it also moves back to the homepage when clicking on the 'Back to list of images' button. 
"""


from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
import random
from random import choice
from PIL import Image
from flask_wtf import FlaskForm


app = Flask(__name__,	
			static_url_path = '', 
			static_folder = 'images',
			template_folder='templates')
Bootstrap = Bootstrap(app)

# dictionary of the images
img_list = {
	'Eastern':'34694102243_3370955cf9_z.jpg',
	'Spreetunnel':'37198655640_b64940bd52_z.jpg',
	'East Side Gallery':'36909037971_884bd535b1_z.jpg',
	'Lombardia, september':'36604481574_c9f5817172_z.jpg',
	'Palazzo Madama': '36885467710_124f3d1e5d_z.jpg',
	'Rijksmuseum library': '37246779151_f26641d17f_z.jpg',
	'Canoeing in Amsterdam': '36523127054_763afc5ed0_z.jpg',
	'Quiet at dawn, Cabo San Lucas' : '35889114281_85553fed76_z.jpg',
	'View from our rental' : '34944112220_de5c2684e7_z.jpg',
	'Someday' : '36140096743_df8ef41874_z.jpg'
}

# get random images from the dictionary using random.choice
@app.route('/')
def home():
	rand_img = []
	for i in range(3):
		r = random.choice(list(img_list.items()))[1]
		if r not in rand_img: rand_img.insert(i, r)
		else:
			r = random.choice(list(img_list.items()))[1]
			if r not in rand_img: rand_img.insert(i, r)


	link1 = '/'+rand_img[0].lower()
	return render_template('home.html', image_file1=rand_img[0], image_file2=rand_img[1], image_file3=rand_img[2])

# make routes and render templates using python decorator
@app.route('/picture/34694102243_3370955cf9_z', methods=['GET','POST'])
def eastern():
	return render_template('eastern.html')

@app.route('/picture/37198655640_b64940bd52_z', methods=['GET','POST'])
def spreetunnel():
	return render_template('spreetunnel.html')

@app.route('/picture/36909037971_884bd535b1_z', methods=['GET','POST'])
def EastSide():
	return render_template('eastside.html')

@app.route('/picture/36604481574_c9f5817172_z', methods=['GET','POST'])
def lombardia():
	return render_template('lombardia.html')

@app.route('/picture/36885467710_124f3d1e5d_z', methods=['GET','POST'])
def palazzo():
	return render_template('palazzo.html')

@app.route('/picture/37246779151_f26641d17f_z', methods=['GET','POST'])
def library():
	return render_template('library.html')

@app.route('/picture/36523127054_763afc5ed0_z', methods=['GET','POST'])
def canoeing():
	return render_template('canoeing.html')

@app.route('/picture/35889114281_85553fed76_z', methods=['GET','POST'])
def quiet():
	return render_template('quiet.html')

@app.route('/picture/34944112220_de5c2684e7_z', methods=['GET','POST'])
def view():
	return render_template('view.html')

@app.route('/picture/36140096743_df8ef41874_z', methods=['GET','POST'])
def someday():
	return render_template('someday.html')




if __name__ == "__main__":
	app.run(debug=True)