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
        # set window titile 
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
      if (self.a == 'none' and (self.line.text() == "Spreetunnel" or self.line.text() == "Berlin" or self.line.text() == "Germany" or self.line.text() == "tunnel" or self.line.text() == "ceiling")):
          im2.show()          
      if (self.a == 'none' and (self.line.text() == "Eastern" or self.line.text() == "Los Angeles" or self.line.text() == "California" or self.line.text() == "building")):
          im1.show()
      if (self.a == 'none' and (self.line.text() == "Eastern" or self.line.text() == "Los Angeles" or self.line.text() == "California" or self.line.text() == "building")):
          im3.show()
      if (self.a == 'none' and (self.line.text() == "Eastern" or self.line.text() == "Los Angeles" or self.line.text() == "California" or self.line.text() == "building")):
          im4.show()
      if (self.a == 'none' and (self.line.text() == "Eastern" or self.line.text() == "Los Angeles" or self.line.text() == "California" or self.line.text() == "building")):
          im5.show()
      if (self.a == 'none' and (self.line.text() == "Eastern" or self.line.text() == "Los Angeles" or self.line.text() == "California" or self.line.text() == "building")):
          im6.show()
      if (self.a == 'none' and (self.line.text() == "Eastern" or self.line.text() == "Los Angeles" or self.line.text() == "California" or self.line.text() == "building")):
          im7.show()
      if (self.a == 'none' and (self.line.text() == "Eastern" or self.line.text() == "Los Angeles" or self.line.text() == "California" or self.line.text() == "building")):
          im8.show()
      if (self.a == 'none' and (self.line.text() == "Eastern" or self.line.text() == "Los Angeles" or self.line.text() == "California" or self.line.text() == "building")):
          im9.show()
      if (self.a == 'none' and (self.line.text() == "Eastern" or self.line.text() == "Los Angeles" or self.line.text() == "California" or self.line.text() == "building")):
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
