from flask import Flask,request
from clients import JokeApi
from clients import Inports

app = Flask(__name__)


@app.route("/random-joke")
def return_joke():
    return JokeApi.get_random_joke()
    
@app.route("/random-5-jokes")
def return_five():
    return JokeApi.five_jokes()        

@app.route("/multi-random-joke")
def multiple_joke():
    data = int(request.args.get('count'))
    count = Inports(data)
    print(count)

    return "Todo...."
    


if __name__=='__main__':
    app.run(debug=False)