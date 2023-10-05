from nodes import MeshNode
from graph import MeshGraph


def main():
    link = 'http://192.168.0.102:80/scan/'
    root_device = MeshNode(link)
    data = root_device.scan_network()
    graph = MeshGraph()
    graph.create_edges(data)
    graph.show()


if __name__ == "__main__":
    main()
