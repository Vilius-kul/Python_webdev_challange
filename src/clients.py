from urllib.parse import urljoin

import requests


class JokeApi:

    base_url = "https://v2.jokeapi.dev/joke/"

    @classmethod
    def get_random_joke(cls):
        endpoint = "Any?blacklistFlags=nsfw,racist,sexist,explicit"
        url = urljoin(cls.base_url, endpoint)
        response = requests.get(url).json()
        print(response)

        joke = ""
        if response["type"] == "twopart":
            joke += f"{response['setup']}... {response['delivery']}"
        else:
            joke += response["joke"]

        return joke

    # Returns 5 random jokes
    @classmethod
    def five_jokes(cls):
        jokes = []
        for j in range(5):
            jokes.append(cls.get_random_joke())

        return jokes

    # Returns multiple random jokes
    @classmethod
    def multiple_jokes(cls, userInput=0):
        jokes = []
        for j in range(userInput):
            jokes.append(cls.get_random_joke())
        return jokes
