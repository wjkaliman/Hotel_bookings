from flask import Flask, render_template, redirect, Blueprint
from flask_pymongo import PyMongo
from flask import Flask, jsonify
import json
from datetime import datetime
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://vdbnoaa.69ws.mongodb.net27017/Project2"
mongo = PyMongo(app)


@app.after_request  # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/scatter")
def scatter():
    return render_template("index2.html")


@app.route("/machine")
def mach():
    print("machine")
    model = load_model("static/data/model.h5")


    # these are not the columns- values of the position of the rows
    new_data = np.array([[33, 25, 1]])
    print(f"Predicted class: {model.predict_classes(new_data)}")
    return render_template("index3.html")


@app.route("/api/bookings")
def landing_data():
    print("bookings")

    print()
    return jsonify()


@app.route("/api/hotel_bookings")
def landingsModified():
    print("hotel_bookings")

    print()


if __name__ == "__main__":
    app.run(debug=True)
