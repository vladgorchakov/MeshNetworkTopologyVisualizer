import requests
import networkx as nx
import matplotlib.pyplot as plt


class MeshGraph:
    def __init__(self):
        self.__points = []
        self.__graph = None

    def create_edges(self, main_node: dict) -> list:
        main_node_id = main_node.get('nodeId')
        if main_node_id:
            subs = main_node.get('subs')
            if subs:
                for sub in subs:
                    self.__points.append((main_node_id, sub['nodeId']))
                    self.create_edges(sub)

        return self.__points

    def __create_nodes_layers(self):
        for layer, nodes in enumerate(nx.topological_generations(self.__graph)):
            for node in nodes:
                print(node, layer)
                self.__graph.nodes[node]["layer"] = layer

    def show(self, title='MESH BSUIR 1-339'):
        self.__graph = nx.DiGraph(self.__points)
        self.__create_nodes_layers()
        pos = nx.multipartite_layout(self.__graph, subset_key="layer")
        fig, ax = plt.subplots()
        nx.draw_networkx(self.__graph, pos=pos, ax=ax, node_size=4000, font_size=10)
        ax.set_title(title)
        fig.tight_layout()
        plt.show()


class MeshDevice:
    def __init__(self, url: str):
        self.__url = url

    def scan_network(self) -> dict:
        response = requests.get(self.__url)
        return response.json()


# data = '{"nodeId":474950769,"root":true,"subs":[{"nodeId":679054265,"subs":[{"nodeId":699587809},{"nodeId":675614937,"subs":[{"nodeId":699587633,"subs":[{"nodeId":697631273,"subs":[{"nodeId":697627909}]}]}]}]}]}'
link = 'http://192.168.0.102:80/scan/'
root_device = MeshDevice(link)
data = root_device.scan_network()
graph = MeshGraph()
graph.create_edges(data)
graph.show()
