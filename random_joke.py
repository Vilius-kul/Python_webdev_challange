from flask import Flask,request
from clients import JokeApi
from schemas import MultipleJokesRequestParams
from pydantic import ValidationError
from translate import JokeTranslator
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
        request_data = MultipleJokesRequestParams(**raw_request)
    except ValidationError as exc:
        return(str(exc))

    return JokeApi.multiple_jokes(request_data.count)
    

@app.route("/multi-language-jokes")
def test_trans():
    raw_request = request.args
    try:
        request_data = MultipleJokesRequestParams(**raw_request)
    except ValidationError as exc:
        return(str(exc))

    string = JokeApi.multiple_jokes(request_data.count)
    return JokeTranslator.get_joke(string)



if __name__=='__main__':
    app.run(debug=False)

