from PyQt5.QtCore import QUrl
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Tarayici(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pyrowser")
        self.setGeometry(100, 100, 800, 600)

        self.tarayici = QWebEngineView()
        self.url_cubugu = QLineEdit()
        self.url_cubugu.setPlaceholderText("https://www.google.com")
        self.git_butonu = QPushButton("Git")

        self.git_butonu.clicked.connect(self.git)
        self.url_cubugu.returnPressed.connect(self.git)

        layout = QVBoxLayout()
        layout.addWidget(self.url_cubugu)
        layout.addWidget(self.git_butonu)
        layout.addWidget(self.tarayici)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.tarayici.load(QUrl("https://www.google.com"))

    def git(self):
        url = self.url_cubugu.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.tarayici.load(QUrl(url))

app = QApplication(sys.argv)
pencere = Tarayici()
pencere.show()
sys.exit(app.exec_())
