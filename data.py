import requests


def fetch_asteroids():
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date=2024-11-26&end_date=2024-12-03&api_key=PYHflNgvgrNRvLuQ39GkOPK2cCcaUXFfKojDSnXe"
    response = requests.get(url)
    data = response.json()
    asteroids = []
    for date, objects in data["near_earth_objects"].items():
        for obj in objects:
            asteroids.append({
                "name": obj["name"],
                "size": obj["estimated_diameter"]["meters"]["estimated_diameter_max"],
                "speed": obj["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"],
                "distance": obj["close_approach_data"][0]["miss_distance"]["kilometers"],
                "date": obj["close_approach_data"][0]["close_approach_date"],
                "hazardous": obj["is_potentially_hazardous_asteroid"]
            })
    return asteroids
