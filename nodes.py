import requests


class MeshNode:
    def __init__(self, url: str):
        self.__url = url

    def scan_network(self) -> dict:
        try:
            response = requests.get(self.__url)
        except requests.exceptions.ConnectionError as error:
            print('Node is not connect:', error, sep='\n')
        else:
            try:
                topology = response.json()
            except requests.exceptions.JSONDecodeError as error:
                print('Response data format is not JSON. Check API endpoint format:', error, sep='\n')
            else:
                return topology
