#Flask app
from flask import Flask
import requests



app = Flask(__name__)

url = 'https://official-joke-api.appspot.com/random_joke'
response = requests.get(url)



@app.route("/")
def hello_world():
    return "<h1>My first flask app!</h1>"

@app.route("/random-joke")
def return_joke():
    return response.json()


if __name__=='__main__':
    app.run(debug=False)