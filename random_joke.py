import re
from flask import Flask
from werkzeug.datastructures import Range
from clients import JokeApi

app = Flask(__name__)

@app.route("/random-joke")
def return_joke():

    joke = JokeApi.get_random_joke()
    
    return f"{joke['setup']}...{joke['punchline']}"

@app.route("/random-5-jokes")
def return_5_jokes():
    jokes = ""
    for i in range(1,6):
        jokes += return_joke()
    return jokes
    
            





if __name__=='__main__':
    app.run(debug=False)