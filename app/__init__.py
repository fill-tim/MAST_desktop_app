from PyQt6.QtWidgets import (
    QApplication,
)

from .widgets import MainWindow


def start_app():
    app = QApplication([])

    window = MainWindow()

    window.show()

    app.exec()
