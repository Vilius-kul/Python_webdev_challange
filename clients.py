import requests
import urllib.parse as urlparse
from urllib.parse import urljoin, parse_qs

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

    #Returns multiple random jokes
    @classmethod
    def multiple_jokes(cls, userInput =0):
        jokes = ""
        for j in range(userInput):
            jokes+= cls.get_random_joke()
        return jokes


    #################one of my attemps####################
    # @staticmethod
    # def input_validator():
    #     while True:
    #     try:
    #         userInput = int(request.args.get('count'))
    #         if userInput < 0 or userInput> 15:
    #             raise ValueError
    #     except ValueError:
    #         print("Invalid input")
    #     else:            
    #         return userInput  






"""
Create a separate endpoint, /multi-random-joke, that can return multiple jokes depending on how many
 the client (requestor) has asked for.
 
 This will involve being able to extract a query parameter from a url and pass it into your flask function.
  A request url may look like:
 
/multi-random-joke?count=3
 
And your API would return three random jokes. 
 
Top tips:
 
* Try to keep your functions in the `random_joke.py` as small as possible. 
Their only job is to consume data from the request, call some other function, then return data back to the client.
* Maybe also place a limit on the maximum number of jokes that can be requested and properly handle invalid counts
 for example a string instead of a number.
"""