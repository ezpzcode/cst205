"""
NAME : YE LIN JOH
DATE : 10/13/2019
COURSE : CST205
PARTNER : WON KYU JEONG
"""

import sys
from PIL import Image, ImageOps
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton, QComboBox, QVBoxLayout
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtCore import pyqtSlot

#open images and assign them to im1-10
im1= Image.open('images/34694102243_3370955cf9_z.jpg','r')
im2= Image.open('images/37198655640_b64940bd52_z.jpg','r')
im3= Image.open('images/36909037971_884bd535b1_z.jpg','r')
im4= Image.open('images/36604481574_c9f5817172_z.jpg','r')
im5= Image.open('images/36885467710_124f3d1e5d_z.jpg','r')
im6= Image.open('images/37246779151_f26641d17f_z.jpg','r')
im7= Image.open('images/36523127054_763afc5ed0_z.jpg','r')
im8= Image.open('images/35889114281_85553fed76_z.jpg','r')
im9= Image.open('images/34944112220_de5c2684e7_z.jpg','r')
im10= Image.open('images/36140096743_df8ef41874_z.jpg','r')


image_info = [
     {
           "id" : "34694102243_3370955cf9_z",
           "title" : "Eastern",
           "flickr_user" : "Sean Davis",
           "tags" : ["Los Angeles", "California", "building"]
      },
      {
           "id" : "37198655640_b64940bd52_z",
           "title" : "Spreetunnel",
           "flickr_user" : "Jens-Olaf Walter",
           "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
      },
      {
           "id" : "36909037971_884bd535b1_z",
           "title" : "East Side Gallery",
           "flickr_user" : "Pieter van der Velden",
           "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
      },
      {
           "id" : "36604481574_c9f5817172_z",
           "title" : "Lombardia, september 2017",
           "flickr_user" : "Mónica Pinheiro",
           "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
      },
      {
           "id" : "36885467710_124f3d1e5d_z",
           "title" : "Palazzo Madama",
           "flickr_user" : "Kevin Kimtis",
           "tags" : [ "Rome", "Italy", "window", "road", "building"]
      },
      {
           "id" : "37246779151_f26641d17f_z",
           "title" : "Rijksmuseum library",
           "flickr_user" : "John Keogh",
           "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
      },
      {
           "id" : "36523127054_763afc5ed0_z",
           "title" : "Canoeing in Amsterdam",
           "flickr_user" : "bdodane",
           "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
      },
      {
           "id" : "35889114281_85553fed76_z",
           "title" : "Quiet at dawn, Cabo San Lucas",
           "flickr_user" : "Erin Johnson",
           "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
      },
      {
           "id" : "34944112220_de5c2684e7_z",
           "title" : "View from our rental",
           "flickr_user" : "Doug Finney",
           "tags" : ["Mexico", "ocean", "beach", "palm"]
      },
      {
           "id" : "36140096743_df8ef41874_z",
           "title" : "Someday",
           "flickr_user" : "Thomas Hawk",
           "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
      }
]

# put filter keys in list to make combobox
manipulation = ['select option', 'sepia', 'negative', 'grayscale', 'thumnail', 'none']


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget) 

        self.setMinimumSize(QSize(320, 140))    
        # set window tite 
        self.setWindowTitle("Image Search Engine")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Image: ')
        # QLineEdit for input text
        self.line = QLineEdit(self) 

        # set location and size of QLineEdit
        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        # set a combobox with items and adjust its size and location 
        self.pycombobox = QComboBox(centralWidget)
        self.pycombobox.addItems(manipulation)
        self.pycombobox.setGeometry(QRect(40, 40, 120, 31))
        self.pycombobox.setObjectName(("comboBox"))
        self.pycombobox.move(120,100)
        self.pycombobox.currentIndexChanged.connect(self.update_ui1) 


       #  pycombobox.currentIndexChanged.connect(self.update_ui)

        # create a button with function and set its size and location
        pybutton = QPushButton('search', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)  
        
        # variable 'a' to determine filters
        self.a = ''


    # put different values to distinguish color filters
    def update_ui1(self):
      my_text = self.pycombobox.currentText()
      my_index = self.pycombobox.currentIndex()
      if my_text == 'none':
        self.a = 'none'
      if my_text == 'sepia':
        self.a = 'sepia'
      if my_text == 'negative':
        self.a = 'negative'
      if my_text == 'grayscale':
        self.a = 'grayscale'  
      if my_text == 'thumnail':
        self.a = 'thumnail'      


    # show images but I could not find out how to check two tags yet.



    def clickMethod(self):
      str_split = self.line.text().split()

      count1 = 0
      count2 = 0
      count3 = 0
      count4 = 0
      count5 = 0
      count6 = 0
      count7 = 0
      count8 = 0
      count9 = 0
      count10 = 0

      for x in str_split:
        if x == "Eastern" or x == "Los Angeles" or x == "California" or x == "building":
          count1 = count1 + 1
        if x == "Spreetunnel" or x == "Berlin" or x == "Germany" or x == "tunnel" or x == "ceiling":
          count2 = count2 + 1
        if x == "East Side Gallery" or x == "Berlin" or x == "wall" or x == "mosaic" or x == "sky" or x == "clouds":
          count3 = count3 + 1
        if x == "Lombardia, september 2017" or x == "Italy" or x == "Lombardia" or x == "alley" or x == "building" or x == "wall":
          count4 = count4 + 1
        if x == "Palazzo Madama" or x == "Rome" or "Italy" or x == "window" or x == "road" or x == "building":
          count5 = count5 + 1
        if x == "Rijksmuseum libarary" or x == "Amsterdam" or x == "Netherlands" or x == "book" or x == "library" or x == "museum":
          count6 = count6 + 1
        if x == "Canoeing in Amsterdam" or x == "Amsterdam" or x == "Netherlands" or x == "canal" or x == "boat":
          count7 = count7 + 1
        if x == "Quiet at dawn, Cabo San Lucas" or x == "Mexico""cabo""beach""cactus" or x == "sunrise":
          count8 = count8 + 1
        if x == "View from our rental" or x == "Mexico" or x == "ocean" or x == "beach" or x == "palm":
          count9 = count9 + 1
        if x == "Someday" or x == "Los Angeles" or x == "Hollywood" or x == "California" or x == "Volkswagen" or x == "Beatle" or x == "car":
          count10 = count10 + 1

      count = []
      count.append(count1)
      count.append(count2)
      count.append(count3)
      count.append(count4)
      count.append(count5)
      count.append(count6)
      count.append(count7)
      count.append(count8)
      count.append(count9)
      count.append(count10)


      alphabet = []

      if (self.a == 'none' and count1 == max(count)):
          alphabet.append("Eastern")
      if (self.a == 'none' and count2 == max(count)):
          alphabet.append("Spreetunnel")
      if (self.a == 'none' and count3 == max(count)):
          alphabet.append("East Side Gallery")
      if (self.a == 'none' and count4 == max(count)):
          alphabet.append("Lombardia, september 2017")
      if (self.a == 'none' and count5 == max(count)):
          alphabet.append("Palazzo Madama")
      if (self.a == 'none' and count6 == max(count)):
          alphabet.append("Rijksmuseum libarary")
      if (self.a == 'none' and count7 == max(count)):
          alphabet.append("Canoeing in Amsterdam")
      if (self.a == 'none' and count8 == max(count)):
          alphabet.append("Quiet at dawn, Cabo San Lucas")
      if (self.a == 'none' and count9 == max(count)):
          alphabet.append("View from our rental")
      if (self.a == 'none' and count10 == max(count)):
          alphabet.append("Someday")



      if (min(sorted(alphabet)) == "Eastern"):
        im1.show()
      if (min(sorted(alphabet)) == "Spreetunnel"):
        im2.show()
      if (min(sorted(alphabet)) == "East Side Gallery"):
        im3.show()
      if (min(sorted(alphabet)) == "Lombardia, september 2017"):
        im4.show()
      if (min(sorted(alphabet)) == "Palazzo Madama"):
        im5.show()
      if (min(sorted(alphabet)) == "Rijksmuseum libarary"):
        im6.show()
      if (min(sorted(alphabet)) == "Canoeing in Amsterdam"):
        im7.show()
      if (min(sorted(alphabet)) == "Quiet at dawn, Cabo San Lucas"):
        im8.show()
      if (min(sorted(alphabet)) == "View from our rental"):
        im9.show()
      if (min(sorted(alphabet)) == "Someday"):
        im10.show()


""" @pyqtSlot()
    def update_ui(self):
        my_text = self.pycombobox.currentText()
        my_index = self.pycombobox.currentIndex()
"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
