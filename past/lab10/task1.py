import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox)
from PyQt5.QtCore import pyqtSlot

my_list = ["Pick a color", "vermillon", "salmon", "khaki", "plum"]
my_RGBdata = ["","(227, 66, 52)","(250, 128, 114)","(240,230,140)","(221, 160, 221)",]
my_HEXdata = ["","#e34234","#fa8072","#f0e78c","#dda0dd"]


class Window1(QWidget):
    def __init__(self):
        super().__init__()

        self.label1 = QLabel('CST 205 Color Exchange!', self)

        self.my_combo_box = QComboBox()
        self.my_combo_box.addItems(my_list)

        self.my_RGB = QLabel('RGB: ', self)
        self.my_HEX = QLabel('Hex: ', self)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.my_RGB)
        self.hbox.addWidget(self.my_HEX)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label1)
        self.vbox.addWidget(self.my_combo_box)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui1)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui2)
        self.my_btn.clicked.connect(self.Window2)
        self.setWindowTitle("Colors!")



    @pyqtSlot()
    def update_ui1(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()
        self.my_RGB.setText(f'RGB: {my_RGBdata[my_index]}')

    def update_ui2(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()
        self.my_HEX.setText(f'HEX: {my_HEXdata[my_index]}')

    def Window2(self):
        i = self.my_combo_box.currentIndex()
        if i == 1:
           w = self.w = Window2()
           self.w.show()
           self.setAutoFillBackground(True)
           p = w.palette()
           p.setColor(w.backgroundRole(), QColor(227, 66, 52))
           w.setPalette(p)
        if i == 2:
           w = self.w = Window2()
           self.w.show()
           self.setAutoFillBackground(True)
           p = w.palette()
           p.setColor(w.backgroundRole(), QColor(250, 128, 114))
           w.setPalette(p)
        if i == 3:
           w = self.w = Window2()
           self.w.show()
           self.setAutoFillBackground(True)
           p = w.palette()
           p.setColor(w.backgroundRole(), QColor(240,230,140))
           w.setPalette(p)
        if i == 4:
           w = self.w = Window2()
           self.w.show()
           self.setAutoFillBackground(True)
           p = w.palette()
           p.setColor(w.backgroundRole(), QColor(221, 160, 221))
           w.setPalette(p)



app = QApplication(sys.argv)
main = Window1()
main.show()
sys.exit(app.exec_())

