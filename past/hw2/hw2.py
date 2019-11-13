"""
Name : YE LIN JOH
Date : 10/05/2019
Course : CST205
Partner : WON KYU JEONG
Description : the code calculates the median of the pixel values retrieved from the images 
  and creates a new image with an unwanted element in the series removed.
"""

from PIL import Image
# define a function named 'median' to calculate the median
def median(val):
  mid = len(val)//2
  return val[mid]

# put images into a dictionary named 'files'
files = {1:"1.png",
     2:"2.png",
     3:"3.png",
     4:"4.png",
     5:"5.png",
     6:"6.png",
     7:"7.png",
     8:"8.png",
     9:"9.png",
     10:"10.png",
     11:"11.png"}
# load the images
im1 = Image.open(files[1])
im2 = Image.open(files[2])
im3 = Image.open(files[3])
im4 = Image.open(files[4])
im5 = Image.open(files[5])
im6 = Image.open(files[6])
im7 = Image.open(files[7])
im8 = Image.open(files[8])
im9 = Image.open(files[9])
im10 = Image.open(files[10])
im11 = Image.open(files[11])
# returns the images' data as lists
list1 = list(im1.getdata())
list2 = list(im2.getdata())
list3 = list(im3.getdata())
list4 = list(im4.getdata())
list5 = list(im5.getdata())
list6 = list(im6.getdata())
list7 = list(im7.getdata())
list8 = list(im8.getdata())
list9 = list(im9.getdata())
list10 = list(im10.getdata())
list11 = list(im11.getdata())

# sorts the data of each lists in sequence and calculates the median, the code iterates over the data from 0th to the last 
count = 0
newim = []
while(count < len(list1)):
  temp = [list1[count],list2[count],list3[count],list4[count],list5[count],list6[count],list7[count],list8[count],list9[count],list10[count],list11[count]]
  temp = sorted(temp)
  pixel = median(temp)
  newim.append(pixel)
  count += 1

# puts the calculated median data into the first image and saves it as 'hw2_nofox.png'
im1.putdata(newim)
im1.save('hw2_nofox.png')