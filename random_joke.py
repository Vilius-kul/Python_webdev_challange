from flask import Flask
from classes import JokeApi

app = Flask(__name__)

@app.route("/random-joke")
def return_joke():

    joke = JokeApi.get_random_joke()
    
    return f"{joke['setup']}...{joke['punchline']}"


if __name__=='__main__':
    app.run(debug=False)