import requests
from urllib.parse import urljoin

class JokeApi:

    base_url = "https://official-joke-api.appspot.com/"

    
    #returns a random joke
    @classmethod
    def get_random_joke(cls):

        endpoint = "random_joke"
        url = urljoin(cls.base_url, endpoint)
        response = requests.get(url)
        setup = response.json()['setup']
        punchline = response.json()['punchline']
        jokes = "{}...  {}".format(setup,punchline)
        
        return jokes
        
    #Returns 5 random jokes
    @classmethod
    def five_jokes(cls):
        jokes =""
        for j in range(6):
            jokes+=cls.get_random_joke()
        
        return jokes

    #Returns multiple random jokes
    @classmethod
    def multiple_jokes(cls, userInput =0):
        jokes = []
        for j in range(userInput):
            jokes.append(cls.get_random_joke())
        return jokes


