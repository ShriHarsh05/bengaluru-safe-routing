import torch
import os
import osmnx as ox

from graph_builder import (
    get_city_graph,
    graph_to_tensors,
    compute_node_features,
    compute_traffic_weights
)

from crime_data import load_crime_data, compute_crime_density
from gnn_model import RiskGNN
from visualization import plot_risk_map

from routing import safest_route, find_nearest_nodes


def main():

    city = "Bengaluru, Karnataka, India"

    # -------------------------------
    # Load Road Network
    # -------------------------------
    G = get_city_graph(city)

    edge_index, edge_weight, node_mapping = graph_to_tensors(G)

    num_nodes = len(node_mapping)

    print("Total nodes:", num_nodes)

    # -------------------------------
    # Node Features
    # -------------------------------
    base_features = compute_node_features(G, node_mapping)

    # -------------------------------
    # Crime Data
    # -------------------------------
    crime_df = load_crime_data()

    crime_density = compute_crime_density(G, node_mapping, crime_df)

    print("Crime density computed:", crime_density.shape)

    # Combine features
    x = torch.cat((base_features, crime_density.unsqueeze(1)), dim=1)

    # -------------------------------
    # Traffic Data
    # -------------------------------
    traffic_weights = compute_traffic_weights(G)

    # -------------------------------
    # Risk Score Caching
    # -------------------------------
    risk_file = "data/risk_scores.pt"

    if os.path.exists(risk_file):

        print("Loading cached risk scores...")

        risk_scores = torch.load(risk_file)

    else:

        print("Computing risk scores...")

        model = RiskGNN(input_dim=5, hidden_dim=16)

        risk_scores = model(x)

        torch.save(risk_scores, risk_file)

        print("Risk scores saved to disk")

    print("Sample scores:", risk_scores[:10])

    # -------------------------------
    # Visualize Risk Map
    # -------------------------------
    plot_risk_map(G, risk_scores)

    # -------------------------------
    # User Input for Routing
    # -------------------------------
    print("\nEnter start location coordinates")

    start_lat = float(input("Start Latitude: "))
    start_lon = float(input("Start Longitude: "))

    print("\nEnter destination coordinates")

    end_lat = float(input("Destination Latitude: "))
    end_lon = float(input("Destination Longitude: "))

    # -------------------------------
    # Find Nearest Graph Nodes
    # -------------------------------
    start_node, end_node = find_nearest_nodes(
        G,
        start_lat,
        start_lon,
        end_lat,
        end_lon
    )

    # -------------------------------
    # Compute Safest Route
    # -------------------------------
    route = safest_route(
        G,
        start_node,
        end_node,
        risk_scores,
        node_mapping
    )

    print("Safest route nodes:", len(route))

    # -------------------------------
    # Plot Route
    # -------------------------------
    ox.plot_graph_route(
        G,
        route,
        route_linewidth=4,
        node_size=0,
        bgcolor="white"
    )


if __name__ == "__main__":
    main()