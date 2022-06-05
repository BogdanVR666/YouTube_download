from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import pytube


def download_video(link: str, path: str, size: tuple, data_format: str):
    print('Downloading...')


class MainWindow(QMainWindow):

    def download(self):
        link = ""
        path = ""
        settings = {'size': (350, 123), 'data_format': 'mp4'}
        download_video(link, path, **settings)

    def __init__(self):
        super().__init__()

        DownloadButton = QPushButton("download".upper())
        DownloadButton.setCheckable(True)
        DownloadButton.clicked.connect(self.download)

        self.setFixedSize(QSize(500, 300))
        self.setWindowTitle('YT download')
        self.setCentralWidget(DownloadButton)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
