#Flask app
from flask import Flask
import requests
import json



app = Flask(__name__)

url = 'https://official-joke-api.appspot.com/random_joke'


@app.route("/random-joke")
def return_joke():
    response = requests.get(url)

    #return api data as json
    api_dict = response.json()

    #using f string to print out values from json()
    return f"{api_dict['setup']}...{api_dict['punchline']}"



if __name__=='__main__':
    app.run(debug=False)