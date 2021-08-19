import requests
import urllib.parse as urlparse
from urllib.parse import urljoin
from pydantic import BaseModel

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
        joke = "{}...  {}\n".format(setup,punchline)
        
        return joke
        
    #Returns 5 random jokes
    @classmethod
    def five_jokes(cls):
        jokes =""
        for j in range(6):
            jokes+=cls.get_random_joke()
        
        return jokes

class Inports(BaseModel):
    count: int



    ##############Ignore fore now################    
    # #Returns multiple random jokes
    # @classmethod
    # def multiple_jokes(cls, userInput =0):
    #     jokes = ""
    #     for j in range(userInput):
    #         jokes+= cls.get_random_joke()
    #     return jokes


