from flask import Flask,request
from clients import JokeApi
from schemas import MultipleJokesRequestParams
from pydantic import ValidationError

app = Flask(__name__)


@app.route("/random-joke")
def return_joke():
    return JokeApi.get_random_joke()
    
@app.route("/random-5-jokes")
def return_five():
    return JokeApi.five_jokes()        

@app.route("/multi-random-joke")
def multiple_joke():
    # Raw query data
    raw_request = request.args
    #Input validation usin pydantic
    try:
        MultipleJokesRequestParams(**raw_request)
    except ValidationError as exc:
        return(str(exc))
    #instanciate object after validation    
    request_data = MultipleJokesRequestParams(**raw_request)
    return JokeApi.multiple_jokes(request_data.count)


if __name__=='__main__':
    app.run(debug=False)

