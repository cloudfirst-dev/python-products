import flask
from flask import request, jsonify
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = {
    '1': {
        'votes': 1
    }
}


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello World</h1>"

@app.route("/review/<path:id>", methods=['GET'])
def reviews(id):
    return jsonify(books[id])

port = os.environ.get('FLASK_PORT') if os.environ.get('FLASK_PORT') is not None else 8080

app.run(host='0.0.0.0', port=port)