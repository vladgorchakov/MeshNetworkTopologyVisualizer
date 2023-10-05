import requests


class MeshNode:
    def __init__(self, url: str):
        self.__url = url

    def scan_network(self) -> dict:
        try:
            topology = requests.get(self.__url).json()
        except requests.exceptions.ConnectionError as error:
            print("Node is not connect!")
            print(error)
        except requests.exceptions.JSONDecodeError as error:
            print("Response is not JSON. Check mesh node API data format!")
            print(error)
        else:
            return topology
