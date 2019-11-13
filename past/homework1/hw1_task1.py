# Name : YE LIN JOH
# Date : 09/22/2019
# Class : CST205 
# Partner : Wonkyu Jeong
# The code makes three lists of red, green, and blue values using pickled 'homework_1_image_matrix.dat',
# then it distributes each values into four intensity bins.


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



# Use numpy module and name it as np
import numpy as np

# Distribute red_val into four ranges of bins
r = np.array(red_val)
np.histogram(r,bins = [0,64,128,192,256]) 
hisred, bins = np.histogram(r, bins = [0,64,128,192,256])

# Distribute green_val into four ranges of bins
g = np.array(green_val)
np.histogram(g,bins = [0,64,128,192,256])
hisgreen, bins = np.histogram(g, bins = [0,64,128,192,256])

# Distribute blue_val into four ranges of bins
b = np.array(blue_val)
np.histogram(b,bins = [0,64,128,192,256])
hisblue, bins = np.histogram(b, bins = [0,64,128,192,256])



# Print out the number of red values in each bins
print("'red': " + str(hisred) + ",")

# Print out the number of green values in each bins
print("'green': " + str(hisgreen) + ",")

# Print out the number of blue values in each bins
print("'blue': " + str(hisblue))
