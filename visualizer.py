import networkx as nx
import matplotlib.pyplot as plt
import json


def create_graph(grapgh, main_node):
    main_node_id = main_node.get('nodeId')
    if main_node_id:
        subs = main_node.get('subs')
        if subs:
            for sub in subs:
                graph.append((main_node_id, sub['nodeId']))
                create_graph(graph, sub)


data = '{"nodeId":474950769,"root":true,"subs":[{"nodeId":679054265,"subs":[{"nodeId":699587809},{"nodeId":675614937,"subs":[{"nodeId":699587633,"subs":[{"nodeId":697631273,"subs":[{"nodeId":697627909}]}]}]}]}]}'
main_dev = json.loads(data)
print(main_dev)
print(type(main_dev))
print(len(main_dev))
graph = []
create_graph(graph, main_dev)
print(graph)
