from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

VERSION = "1.0.0"

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/api/recommend", methods=["POST"])
def recomend():
    body = request.get_json(force=True)
    songs = body['songs']

    FILE = open('/data/model_rules', 'rb')

    store = pickle.load(FILE)

    rules = store['rules']
    createdAt = store['createdAt']

    recommendation = set(songs)

    for rule in rules:
        for song in songs:
            if song in rule[0]:
                for recommendSound in rule[1]:
                    recommendation.add(recommendSound)

    FILE.close()

    recommendation = list(recommendation)
    return jsonify({
        "songs": recommendation,
        "version": VERSION,
        "model_date": createdAt
    })

app.run(host='0.0.0.0', port=52023)