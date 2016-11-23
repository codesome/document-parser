from flask import Flask,request,jsonify
from parser import *

app = Flask(__name__)

@app.route("/")
def home_handler():
    return 'Welcome to parser<br><a href="https://github.com/thecodesome/parser">Click here</a> for more info'

@app.route("/parse")
def parse_handler():
    """ To handle requests for parse """
    data = parse(request.args)
    if data:
    	return jsonify( **data )
    else:
    	return "null"

@app.route("/topics")
def topic_handler():
    """ To handle requests for topics """
    data = topics(request.args.get("str"))
    if data:
	    return jsonify( **data )
    else:
    	return "null"

if __name__ == "__main__":
	app.run(port=3000)