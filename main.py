import webbrowser

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
import sys

weatherLink = 'https://weather.com/weather/today/l/51.25,22.49?par=google&temp=c'
musicLink = 'https://www.spotify.com/'
videoLink = 'https://www.netflix.com/pl'

class MainWindow(QWidget):
    emitMsg = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setup()

    def weatherAction(self):
        webbrowser.open(weatherLink)

    def musicAction(self):
        webbrowser.open(musicLink)

    def videoAction(self):
        webbrowser.open(videoLink)

    def setup(self):
        grid = QGridLayout()

        self.weather = QPushButton("wather",self)
        self.music = QPushButton("music",self)
        self.video = QPushButton("video",self)

        self.weather.clicked.connect(self.weatherAction)
        self.music.clicked.connect(self.musicAction)
        self.video.clicked.connect(self.videoAction)

        grid.addWidget(self.weather, 0, 0)
        grid.addWidget(self.music, 0, 1)
        grid.addWidget(self.video, 0, 2)

        self.weatherLabel = QLabel("Weather link:",self)
        self.musicLabel = QLabel("Music link:",self)
        self.videoLabel = QLabel("Video link:",self)

        self.changeWeatherLink = QLineEdit()
        self.changeMusicLink = QLineEdit()
        self.changeVideoLink = QLineEdit()

        grid.addWidget(self.weatherLabel, 1, 0)
        grid.addWidget(self.musicLabel, 2, 0)
        grid.addWidget(self.videoLabel, 3, 0)

        grid.addWidget(self.changeWeatherLink, 1, 1)
        grid.addWidget(self.changeMusicLink, 2, 1)
        grid.addWidget(self.changeVideoLink, 3, 1)

        self.changeWeatherLink.setMaximumWidth(200)
        self.changeMusicLink.setMaximumWidth(200)
        self.changeVideoLink.setMaximumWidth(200)

        self.weather.setMaximumHeight(100)
        self.weather.setMaximumWidth(100)
        self.music.setMaximumHeight(100)
        self.music.setMaximumWidth(100)
        self.video.setMaximumHeight(100)
        self.video.setMaximumWidth(100)

        self.setLayout(grid)
        self.setGeometry(20, 20, 300, 350)
        self.setWindowTitle("asystent")
        self.show()


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
