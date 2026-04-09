import osmnx as ox
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm


def plot_risk_map(G, risk_scores):

    print("Generating risk map...")

    risk = risk_scores.detach().numpy().flatten()

    risk = (risk - risk.min()) / (risk.max() - risk.min())

    cmap = cm.get_cmap("RdYlGn_r")

    node_colors = [cmap(r) for r in risk]

    fig, ax = ox.plot_graph(
        G,
        node_color=node_colors,
        node_size=6,
        edge_linewidth=0.2,
        bgcolor="white",
        show=False,
        close=False
    )

    plt.title("Bengaluru Intersection Risk Map")

    plt.show()