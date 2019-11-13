import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import pyqtSlot

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		vbox = QVBoxLayout()
		self.my_btn1 = QPushButton("Button 1", self)
		self.my_lbl1 = QLabel('Button 1 not clicked')
		self.my_btn1.clicked.connect(self.on_click1)		
		vbox.addWidget(self.my_btn1)		
		vbox.addWidget(self.my_lbl1)

		self.my_btn2 = QPushButton("Button 2", self)
		self.my_lbl2 = QLabel('Button 2 not clicked')
		self.my_btn2.clicked.connect(self.on_click2)
		vbox.addWidget(self.my_btn2)
		vbox.addWidget(self.my_lbl2)
		
		self.setLayout(vbox)
		
	@pyqtSlot()
	def on_click1(self):
		self.my_lbl1.setText('Button 1 clicked')
	def on_click2(self):
		self.my_lbl2.setText('Button 2 clicked')

app = QApplication(sys.argv)
main_win = MainWindow()
main_win.show()
sys.exit(app.exec_())