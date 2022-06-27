from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import *
from pytube import YouTube
import asyncio


class MainWindow(QMainWindow):
    _link = str()

    def __init__(self):
        super().__init__()

        self.percent_loaded = 0

        DownloadButton = QPushButton("download".upper())
        DownloadButton.setCheckable(True)
        DownloadButton.clicked.connect(self.download)

        self.progressbar = QProgressBar(self)
        self.progressbar.setValue(self.percent_loaded)

        self.setFixedSize(QSize(500, 300))
        self.setWindowTitle('YT download')
        self.link = QLineEdit()
        self.link.textChanged.connect(self.setLink)

        layout = QVBoxLayout()
        layout.addWidget(self.link)
        layout.addWidget(self.progressbar)
        layout.addWidget(DownloadButton)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def upgrade(self, video, arg2, progress_end):
        percent = 100 - int(progress_end / (video.filesize / 100))
        print(percent)
        self.progressbar.setValue(percent)

    def download(self):
        link = MainWindow._link
        print(link)
        path = 'D:/Code'
        settings = {'res': "720p", 'file_extension': 'mp4'}
        video = YouTube(link, on_progress_callback=self.upgrade)
        video.streams.filter(**settings).order_by('fps').first().download(path)

    @staticmethod
    def setLink(link):
        MainWindow._link = link

    @staticmethod
    def getLink():
        print(MainWindow._link)
        return MainWindow._link

    def setProgressBar(self, value):
        self.progressbar.setValue(value)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
