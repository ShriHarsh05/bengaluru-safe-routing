import pandas as pd
import torch


def load_crime_data():

    df = pd.read_csv("data/bengaluru_crime.csv")

    return df


def compute_crime_density(G, node_mapping, crime_df):

    densities = []

    for node in node_mapping:

        lat = G.nodes[node]["y"]
        lon = G.nodes[node]["x"]

        nearby = crime_df[
            (abs(crime_df["latitude"] - lat) < 0.01) &
            (abs(crime_df["longitude"] - lon) < 0.01)
        ]

        densities.append(len(nearby))

    return torch.tensor(densities, dtype=torch.float)