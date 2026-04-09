import osmnx as ox
import torch
import random
from traffic_data import get_traffic_speed


import osmnx as ox
import os

def get_city_graph(city):

    graph_file = "data/bengaluru_graph.graphml"

    # If graph already exists → load it
    if os.path.exists(graph_file):

        print("Loading saved road network...")

        G = ox.load_graphml(graph_file)

    else:

        print("Downloading road network...")

        G = ox.graph_from_place(city, network_type="drive", simplify=True)

        print("Saving graph for future runs...")

        ox.save_graphml(G, graph_file)

    print("Nodes:", len(G.nodes))
    print("Edges:", len(G.edges))

    return G

def graph_to_tensors(G):

    nodes = list(G.nodes)

    node_mapping = {node: i for i, node in enumerate(nodes)}

    edge_index = []
    distances = []

    for u, v, data in G.edges(data=True):

        edge_index.append([node_mapping[u], node_mapping[v]])

        distance = data.get("length", 1)

        distances.append(distance)

    edge_index = torch.tensor(edge_index).t().contiguous()

    edge_weight = torch.tensor(distances, dtype=torch.float)

    print("Edge tensor shape:", edge_index.shape)

    return edge_index, edge_weight, node_mapping


def compute_node_features(G, node_mapping):

    print("Computing node features...")

    degree = dict(G.degree)

    features = []

    for node in node_mapping:

        deg = degree[node]

        feature = [
            deg,
            deg / 10,
            deg ** 2,
            1
        ]

        features.append(feature)

    x = torch.tensor(features, dtype=torch.float)

    print("Node feature tensor:", x.shape)

    return x


def compute_traffic_weights(G):

    print("Fetching sampled traffic data...")

    sampled_speeds = {}

    nodes = list(G.nodes)

    sample_nodes = random.sample(nodes, 100)

    for node in sample_nodes:

        lat = G.nodes[node]["y"]
        lon = G.nodes[node]["x"]

        speed = get_traffic_speed(lat, lon)

        sampled_speeds[node] = speed

    weights = []

    for u, v, data in G.edges(data=True):

        distance = data.get("length", 1)

        speed = random.choice(list(sampled_speeds.values()))

        weight = distance / max(speed, 1)

        weights.append(weight)

    return torch.tensor(weights, dtype=torch.float)