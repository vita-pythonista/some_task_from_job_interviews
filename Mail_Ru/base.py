import requests
import json

class BaseMethod:

    def __init__(self, url):
        self.url = url
        self.api_key = 'test'

    def get_places_of_interests(self, q, **other_parameters):
        params = {
            'api_key': self.api_key,
            'q': q
            }
        params.update(other_parameters)
        resp = requests.get(url=self.url + "/v3/places", params=params)
        return resp