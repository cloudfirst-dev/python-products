import flask
from flask import request, jsonify
import requests
import os


app = flask.Flask(__name__)
app.config["DEBUG"] = True

ratingPort = os.environ.get('RATING_PORT') if os.environ.get('RATING_PORT') is not None else '8080'
ratingHost = os.environ.get('RATING_HOST') if os.environ.get('RATING_HOST') is not None else 'rating'


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello World</h1>"

@app.route("/product/<path:id>", methods=['GET'])
def reviews(id):
    return jsonify({
        'id': id,
        'votes': requests.get("http://" + ratingHost + ":" + ratingPort + "/review/1").json()['votes']
    })

port = os.environ.get('FLASK_PORT') if os.environ.get('FLASK_PORT') is not None else 8080

app.run(host="0.0.0.0", port=port)