import requests


class MeshGraph:
    def __init__(self):
        self.__points = []

    def create_points_from_maps(self, main_node: dict) -> list:
        main_node_id = main_node.get('nodeId')
        if main_node_id:
            subs = main_node.get('subs')
            if subs:
                for sub in subs:
                    self.__points.append((main_node_id, sub['nodeId']))
                    self.create_points_from_maps(sub)

        return self.__points


class MeshDevice:
    def __init__(self, url: str):
        self.__url = url

    def get_mesh_map(self) -> dict:
        response = requests.get(self.__url)
        return response.json()


# data = '{"nodeId":474950769,"root":true,"subs":[{"nodeId":679054265,"subs":[{"nodeId":699587809},{"nodeId":675614937,"subs":[{"nodeId":699587633,"subs":[{"nodeId":697631273,"subs":[{"nodeId":697627909}]}]}]}]}]}'
link = 'http://192.168.0.102:80/scan/'
root_device = MeshDevice(link)
data = root_device.get_mesh_map()
graph = MeshGraph()
print(graph.create_points_from_maps(data))
