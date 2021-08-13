from flask import Flask,request
from clients import JokeApi

app = Flask(__name__)


@app.route("/random-joke")
def return_joke():
    return JokeApi.get_random_joke()
    
@app.route("/random-5-jokes")
def return_five():
    return JokeApi.five_jokes()        

@app.route("/multi-random-joke")
def multiple_joke():
    userInput = int(request.args.get('count'))
    return JokeApi.multiple_jokes(userInput)



###################Stuck####################################
# def input_validator():
#     while True:
#         try:
#             userInput = int(request.args.get('count'))
#             if userInput < 0 or userInput> 15:
#                 raise ValueError
#         except ValueError:
#             print("Invalid input")
#         else:            
#             return userInput



            

    
            





if __name__=='__main__':
    app.run(debug=False)