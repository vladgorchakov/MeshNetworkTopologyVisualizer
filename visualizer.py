import requests


class MeshGraph:
    def __init__(self, points):
        self.points = points


class MeshDevice:
    def __init__(self, url: str):
        self.__url = url

    def get_mesh_map(self) -> dict:
        response = requests.get(self.__url)
        return response.json()


def create_graph(grapgh, main_node):
    main_node_id = main_node.get('nodeId')
    if main_node_id:
        subs = main_node.get('subs')
        if subs:
            for sub in subs:
                graph.append((main_node_id, sub['nodeId']))
                create_graph(graph, sub)


# data = '{"nodeId":474950769,"root":true,"subs":[{"nodeId":679054265,"subs":[{"nodeId":699587809},{"nodeId":675614937,"subs":[{"nodeId":699587633,"subs":[{"nodeId":697631273,"subs":[{"nodeId":697627909}]}]}]}]}]}'
graph = []
link = 'http://192.168.0.102:80/scan/'
data = get_mesh_topology_json(link)

create_graph(graph, data)
print(graph)
