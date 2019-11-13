# Name : YE LIN JOH
# Date : 09/22/2019
# Class : CST205 
# Partner : Wonkyu Jeong
# The code makes three lists of red, green, and blue values using pickled 'homework_1_image_matrix.dat',
# and it generates three SVG files of historams, showing the distribution of red, green, and blue intensities.


# Use hw1_hist_plotter module and name it as hp
import hw1_hist_plotter as hp



# Using pickle module, load the binary data file 'homework_1_image_matrix.dat'
import pickle
with open("image_matrix","rb") as f:
	matrix = pickle.load(f)

# Separate the red values from the data and put them into red_val list
red_val = []
for x in matrix:
	for y in x:
		red_val.append(y[0])

# Separate the green values from the data and put them into green_val list
green_val = []
for x in matrix:
	for y in x:
		green_val.append(y[1])

# Separate the blue values from the data and put them into blue_val list
blue_val = []
for x in matrix:
	for y in x:
		blue_val.append(y[2])



# Make a list of three separated lists of red, green, and blue values
list = [red_val, green_val, blue_val]

# Using 'hist_plotter' function in hp, create three SVG files of R,G,B histograms
hp.hist_plotter(list)