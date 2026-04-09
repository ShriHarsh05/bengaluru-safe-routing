import pandas as pd
import random

center_lat = 12.9716
center_lon = 77.5946

points = []

for _ in range(800):   # approximate crime density

    lat = center_lat + random.uniform(-0.1, 0.1)
    lon = center_lon + random.uniform(-0.1, 0.1)

    points.append(["crime", lat, lon])

df = pd.DataFrame(points, columns=["crime_type", "latitude", "longitude"])

df.to_csv("data/bengaluru_crime.csv", index=False)

print("Crime points generated")