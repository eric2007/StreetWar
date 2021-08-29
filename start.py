from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QComboBox, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import sys, lxml
import main
class Start(QWidget):
    def __init__(self):
        self.file = ''
        self.tree = lxml.etree
        super().__init__()
        self.setWindowTitle('Street War')
        self.setFixedSize(480,320)
        self.pale = QPalette()
        self.pale.setBrush(QPalette.Background, QBrush(QPixmap('./assets/background.png')))
        self.setPalette(self.pale)
        self.fileButton  = QPushButton('Open Map', self)
        self.fileButton.move(180,100)
        self.fileButton.clicked.connect(self.openFile)
        self.fileLabel = QLabel('None', self)
        self.fileLabel.move(300,100)
        self.DifficultyBox  = QComboBox(self)
        self.DifficultyBox.move(180, 140)
        self.DifficultyBox.addItems(['Easy', 'Medium', 'Hard'])
        # self.DifficultyBox.
        self.startButton = QPushButton('Start', self)
        self.startButton.move(180, 180)
        self.startButton.clicked.connect(self.start)
        self.show()
    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open map', '.', 'OpenStreetMap File(*.osm)')
        self.fileLabel.setText(fname[0].split('/')[-1])
        self.file = fname[0]
    def start(self):
        if not self.file:
            QMessageBox.information(self,'Street War', "Please set map file！",QMessageBox.Yes | QMessageBox.No)
            return
        self.hide()
        self.main = main.Main(0, self.file)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = Start()
    sys.exit(app.exec())