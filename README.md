\# Bengaluru Safe Routing using Graph Neural Networks



\## Overview



Urban travel in unfamiliar cities can expose travelers to potential safety risks such as crime-prone areas, poorly connected road segments, or high traffic congestion. Traditional navigation systems typically focus on minimizing travel time or distance without considering safety-related factors.



This project introduces a \*\*safety-aware navigation framework\*\* that evaluates road networks using \*\*Graph Neural Networks (GNNs)\*\* and integrates \*\*crime statistics, traffic conditions, and road network topology\*\* to generate safer travel routes.



The system models the transportation network as a \*\*graph\*\*, where intersections represent nodes and roads represent edges. Risk scores are computed for each intersection, enabling the generation of a \*\*city-wide risk map\*\* and identification of safer travel paths.



The project currently focuses on \*\*Bengaluru, India\*\*, but the framework can be adapted for other cities.



\---



\# Features



\* Builds a \*\*road network graph\*\* from OpenStreetMap data.

\* Integrates \*\*crime data\*\* to identify high-risk areas.

\* Fetches \*\*traffic information\*\* from the TomTom API.

\* Uses a \*\*Graph Neural Network model\*\* to estimate intersection risk scores.

\* Generates a \*\*city-wide safety risk map\*\*.

\* Computes \*\*safest routes between two locations\*\*.

\* Implements \*\*caching mechanisms\*\* to improve performance.



\---



\# System Architecture



User Input (Start + Destination)

↓

Road Network Graph (OpenStreetMap)

↓

Traffic Data Integration (TomTom API)

↓

Crime Data Integration

↓

Graph Neural Network Risk Prediction

↓

City Risk Map Generation

↓

Safety-Aware Route Computation



\---



\# Project Structure



```

bengaluru-safe-routing

│

├── main.py                # Main execution script

├── graph\_builder.py       # Road network construction

├── routing.py             # Safety-aware routing algorithm

├── gnn\_model.py           # Risk prediction model

├── visualization.py       # Risk map visualization

├── traffic\_data.py        # TomTom traffic API integration

├── crime\_data.py          # Crime density computation

│

├── data

│   ├── bengaluru\_crime.csv

│   └── crime/             # Crime datasets

│

├── requirements.txt

└── README.md

```



\---



\# Technologies Used



Python Libraries:



\* osmnx

\* networkx

\* pandas

\* numpy

\* torch

\* matplotlib

\* scikit-learn

\* requests



Data Sources:



\* OpenStreetMap (road network data)

\* NCRB Crime Dataset

\* TomTom Traffic API



\---



\# Installation



Clone the repository:



```bash

git clone https://github.com/ShriHarsh05/bengaluru-safe-routing.git

cd bengaluru-safe-routing

```



Create a virtual environment:



```bash

python -m venv venv

```



Activate the environment:



Windows:



```bash

venv\\Scripts\\activate

```



Install dependencies:



```bash

pip install -r requirements.txt

```



\---



\# Running the Project



Execute the main script:



```bash

python main.py

```



The program will:



1\. Load or download the Bengaluru road network.

2\. Compute crime density features.

3\. Sample traffic data.

4\. Generate intersection risk scores.

5\. Display a city-wide risk map.

6\. Ask the user for start and destination coordinates.

7\. Compute and visualize the safest route.



Example input:



```

Start Latitude: 12.9716

Start Longitude: 77.5946

Destination Latitude: 12.9352

Destination Longitude: 77.6245

```



\---



\# Example Output



The system generates:



\* A \*\*risk heatmap of Bengaluru road intersections\*\*

\* A \*\*visualized safest route between two locations\*\*



\---



\# Performance Optimizations



To improve runtime efficiency the system implements:



Graph Caching

The road network is stored locally to avoid repeated downloads.



Risk Score Caching

Computed risk scores are saved and reused in future runs.



Traffic Sampling

Instead of querying traffic data for every road segment, sampled traffic points approximate city-wide conditions.



\---



\# Research Applications



This framework can support:



\* Smart city mobility planning

\* Safety-aware navigation systems

\* Crime hotspot detection

\* Urban transportation analytics



\---



\# Future Improvements



Possible future extensions include:



\* Interactive web-based map interface

\* Real-time traffic streaming

\* Advanced Graph Convolution Networks

\* Multi-city support

\* Mobile application integration



\---



\# License



This project is released under the MIT License.



\---



\# Author



Shriharsh S Kotecha



Project: Intelligent Compression to Maximize Cloud Storage Utilization / Safety-Aware Urban Navigation



