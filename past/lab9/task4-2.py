import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDial, QHBoxLayout, QSpinBox
class Form(QWidget):
	def __init__(self):
		 super().__init__()
		 self.dial = QDial()
		 self.dial.setNotchesVisible(True)
		 self.spinbox = QSpinBox()
		 layout = QHBoxLayout()
		 layout.addWidget(self.dial)
		 layout.addWidget(self.spinbox)
		 self.setLayout(layout)
		 self.setWindowTitle("Signals and Slots")
		 self.dial.valueChanged.connect(self.spinbox.setValue)
		 self.spinbox.valueChanged.connect(self.dial.setValue)
app = QApplication(sys.argv)
ex = Form()
ex.show()
sys.exit(app.exec_())