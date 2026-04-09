import networkx as nx
import numpy as np


def safest_route(G, start_node, end_node, risk_scores, node_mapping):

    reverse_mapping = {v: k for k, v in node_mapping.items()}

    for node_id, score in enumerate(risk_scores):

        node = reverse_mapping[node_id]

        # G.nodes[node]["risk"] = float(score)
        G.nodes[node]["risk"] = float(score.detach())

    path = nx.shortest_path(G, start_node, end_node, weight="risk")

    return path

from osmnx.distance import nearest_nodes


def find_nearest_nodes(G, start_lat, start_lon, end_lat, end_lon):

    start_node = nearest_nodes(G, start_lon, start_lat)

    end_node = nearest_nodes(G, end_lon, end_lat)

    return start_node, end_node

