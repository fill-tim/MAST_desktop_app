import requests
from ..config import SERVER_URL, DATA_GET_URL, DATA_POST_URL


class DataService:
    def __init__(self):
        pass

    def get(self):
        return requests.get(SERVER_URL + DATA_GET_URL)

    def post(self, data):
        return requests.post(SERVER_URL + DATA_POST_URL, json=data)
