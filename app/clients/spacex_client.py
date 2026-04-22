import requests

BASE_URL = "https://api.spacexdata.com/v4"


class SpaceXClient:

    def get_upcoming_launches(self):
        return requests.get(f"{BASE_URL}/launches/upcoming").json()

    def get_past_launches(self):
        return requests.get(f"{BASE_URL}/launches/past").json()

    def get_rockets(self):
        return requests.get(f"{BASE_URL}/rockets").json()