from PyQt6.QtCore import QDate, QTime, QStringListModel
from PyQt6.QtWidgets import QMessageBox

from ..api.v1.data_service import DataService


class DataHandlers:
    def __init__(self):
        self._data_service = DataService()

    def post_request(self, line_edit, window):
        try:
            window.click_count += 1

            text = line_edit.text()

            msg = QMessageBox(window)
            msg.setWindowTitle("Уведомление")

            date = QDate.currentDate().toString()
            time = QTime.currentTime().toString()

            data = {
                "text": text,
                "date": date,
                "time": time,
                "click_count": window.click_count,
            }

            response = self._data_service.post(data=data)

            if response.status_code == 201:

                msg.setText("Успешно добавлено!")
                msg.exec()

            else:
                response_text = response.json()["detail"]

                msg.setText(response_text)
                msg.exec()

        except Exception as error:
            print(error)

    def get_request(self, list_view, window):
        try:
            response = self._data_service.get()

            if response.status_code == 200:

                data = response.json()

                array = []

                for item in data:
                    array.append(
                        f"{item['text']} - {item['date']} - {item['time']} - {item['click_count']}"
                    )

                model = QStringListModel()

                model.setStringList(array)

                list_view.setModel(model)

            else:
                msg = QMessageBox(window)

                msg.setWindowTitle("Уведомление")

                msg.setText("Что-то пошло не так(")
                msg.exec()
        except Exception as error:
            print(error)
