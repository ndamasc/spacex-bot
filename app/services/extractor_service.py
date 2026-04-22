from app.clients.spacex_client import SpaceXClient


class ExtractorService:

    def __init__(self):
        self.client = SpaceXClient()

    def collect(self):
        return {
            "upcoming": self.client.get_upcoming_launches(),
            "past": self.client.get_past_launches(),
            "rockets": self.client.get_rockets()
        }