import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

my_qt_app = QApplication(sys.argv)

my_window = QWidget()

my_window.setGeometry(0,0,400,300)

my_window.setWindowTitle('task2')

my_label = QLabel(my_window)
my_label.setText('YE LIN JOH')

my_window.show()
sys.exit(my_qt_app.exec_())