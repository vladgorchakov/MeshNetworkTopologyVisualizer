import networkx as nx
import matplotlib.pyplot as plt


class MeshGraph:
    def __init__(self):
        self.__edges = []
        self.__graph = None
        self.__fig = None
        self.__ax = None

    def create_edges(self, main_node: dict) -> list:
        main_node_id = main_node.get('nodeId')
        if main_node_id:
            subs = main_node.get('subs')
            if subs:
                for sub in subs:
                    self.__edges.append((main_node_id, sub['nodeId']))
                    self.create_edges(sub)

        return self.__edges

    def __create_nodes_layers(self):
        for layer, nodes in enumerate(nx.topological_generations(self.__graph)):
            for node in nodes:
                print(node, layer)
                self.__graph.nodes[node]["layer"] = layer

    def show(self, title='MESH BSUIR 1-339'):
        self.__graph = nx.DiGraph(self.__edges)
        self.__create_nodes_layers()
        pos = nx.multipartite_layout(self.__graph, subset_key="layer")
        self.__fig, self.__ax = plt.subplots()
        nx.draw_networkx(self.__graph, pos=pos, ax=self.__ax, node_size=4000, font_size=10)
        self.__ax.set_title(title)
        self.__fig.tight_layout()
        plt.show()
