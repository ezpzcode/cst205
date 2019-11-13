import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

my_qt_app = QApplication(sys.argv)

my_window = QWidget()
my_window.setWindowTitle('MonaLisa')

picture_label = QLabel(my_window)
my_image = QPixmap('mona.jpg')
picture_label.setPixmap(my_image)

my_window.resize(my_image.width(),my_image.height())


my_window.show()

sys.exit(my_qt_app.exec_())