import random

from flask import Flask, jsonify, request

app = Flask(__name__)

ACTIVITIES = [
    {"activity": "Look away from your screen and rest your eyes.", "minutes": 1},
    {"activity": "Stand up and stretch.", "minutes": 2},
    {"activity": "Refill your water bottle and have a drink.", "minutes": 3},
    {"activity": "Listen to a favorite song.", "minutes": 5},
    {"activity": "Tidy your desk.", "minutes": 5},
    {"activity": "Take a short walk.", "minutes": 10},
    {"activity": "Draw or doodle on paper.", "minutes": 10},
    {"activity": "Read something for fun.", "minutes": 15},
    {"activity": "Take a longer walk outside.", "minutes": 20},
]


@app.after_request
def allow_frontend(response):
    # Let a separate webpage read this public API.
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.get("/break")
def get_break():
    minutes = request.args.get("minutes", type=int)
    if minutes is None or minutes < 1:
        return jsonify(error="Enter a positive whole number of minutes."), 400

    available = [activity for activity in ACTIVITIES if activity["minutes"] <= minutes]
    return jsonify(random.choice(available))


if __name__ == "__main__":
    app.run()
