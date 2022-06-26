from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from pytube import YouTube


def upgrade(video, arg2, progress_end):
    (100 - int(progress_end / (video.filesize / 100)))


def download(link):
    path = 'D:/Code'
    settings = {'res': "720p", 'file_extension': 'mp4'}
    video = YouTube(link, on_progress_callback=upgrade)
    video.streams.filter(**settings).order_by('fps').first().download(path)


def download_button():
    download(MainWindow.getLink())


class MainWindow(QMainWindow):
    _link = str()

    def __init__(self):
        super().__init__()

        DownloadButton = QPushButton("download".upper())
        DownloadButton.setCheckable(True)
        DownloadButton.clicked.connect(download_button)

        progressbar = QProgressBar(self)
        progressbar.resize(50, 50, 250, 30)
        progressbar.setValue(0)

        self.setFixedSize(QSize(500, 300))
        self.setWindowTitle('YT download')
        self.link = QLineEdit()
        self.link.textChanged.connect(self.setLink)

        layout = QVBoxLayout()
        layout.addWidget(self.link)
        layout.addWidget(DownloadButton)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

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
