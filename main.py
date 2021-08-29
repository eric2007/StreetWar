from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QComboBox, QFileDialog, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import sys
class Main(QMainWindow):
    def __init__(self, type, file):
        self.file = open(file, 'r')
        super().__init__()
        self.setWindowTitle('Street War')
        self.resize(1280,960)
        self.BigButton = QPushButton('+', self)
        self.BigButton.setGeometry(5,5,20,20)
        self.SmallButton = QPushButton('-', self)
        self.SmallButton.setGeometry(5,30,20,20)
        self.show()
        self.MinLat = 
    def resizeEvent(self, event):
        print(event.size().width(), event.size().height())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main(0, './map.osm')
    sys.exit(app.exec_())