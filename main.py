from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from pytube import YouTube


def download():

    path = 'D:/Code'
    settings = {'res': "720p", 'mine_type': 'video/mp4'}
    video = YouTube(link)
    video.streams.filter(**settings).order_by('fps').first().download(path)


class MainWindow(QMainWindow):
    _link = str()

    def __init__(self):
        super().__init__()

        DownloadButton = QPushButton("download".upper())
        DownloadButton.setCheckable(True)
        DownloadButton.clicked.connect(download)

        self.setFixedSize(QSize(500, 300))
        self.setWindowTitle('YT download')
        self.input = QLineEdit()
        self.input.textChanged.connect(self.setLink)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(DownloadButton)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    @staticmethod
    def setLink(link):
        MainWindow._link = link


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
