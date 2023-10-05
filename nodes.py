import requests


class MeshNode:
    def __init__(self, url: str):
        self.__url = url

    def scan_network(self) -> dict:
        response = requests.get(self.__url)
        return response.json()
