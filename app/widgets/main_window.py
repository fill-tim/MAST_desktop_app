import functools
from PyQt6.QtWidgets import (
    QWidget,
    QLineEdit,
    QListView,
    QPushButton,
    QVBoxLayout,
)

from ..handlers.data_handlers import DataHandlers


class MainWindow(
    QWidget,
):
    def __init__(self):
        self._data_handler = DataHandlers()
        super().__init__()

        self.line_edit = QLineEdit()
        self.list_view = QListView()
        self.list_view.setViewMode(QListView.ViewMode.ListMode)
        self.post_button = QPushButton("Добавить")
        self.get_button = QPushButton("Вывести")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.list_view)
        self.layout.addWidget(self.post_button)
        self.layout.addWidget(self.get_button)

        self.setLayout(self.layout)

        self.setWindowTitle("Клиентское приложение")

        self.click_count = 0

        self.post_button.clicked.connect(
            functools.partial(self._data_handler.post_request, self.line_edit, self)
        )
        self.get_button.clicked.connect(
            functools.partial(self._data_handler.get_request, self.list_view, self)
        )
