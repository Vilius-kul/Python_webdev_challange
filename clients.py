import requests
from urllib.parse import urljoin

class JokeApi:

    base_url = "https://official-joke-api.appspot.com/"

    @classmethod
    def get_random_joke(cls):

        endpoint = "random_joke"
        url = urljoin(cls.base_url, endpoint)
        response = requests.get(url)
        
        return response.json()
