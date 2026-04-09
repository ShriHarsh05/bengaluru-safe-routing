import requests
import random

TOMTOM_API_KEY = "8zlk7FRkuul3xaM17WonsYJB0Cj9dpkV"


def get_traffic_speed(lat, lon):

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"

    params = {
        "point": f"{lat},{lon}",
        "key": TOMTOM_API_KEY
    }

    try:

        response = requests.get(url, params=params, timeout=5)

        data = response.json()

        speed = data["flowSegmentData"]["currentSpeed"]

        return speed

    except:

        return random.uniform(20, 50)

def get_traffic_speed(lat, lon):

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"

    params = {
        "point": f"{lat},{lon}",
        "key": TOMTOM_API_KEY
    }

    try:

        response = requests.get(url, params=params, timeout=5)

        data = response.json()

        speed = data["flowSegmentData"]["currentSpeed"]

        return speed

    except:

        # fallback random traffic speed
        return random.uniform(20, 50)