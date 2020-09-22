import numpy as np
import pandas as pd
from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    redirect,
    render_template_string,
    url_for,
)

import pickle


app = Flask("Sneaker Price Predictor")
# HACK - commenting out model load since it's not available on github right now
# model = pickle.load(open("/Users/logno/Documents/Home/BAF1/model.pkl", "rb"))


@app.route("/")
def home():
    # Main page. The line below throws an error and idk why
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # TODO - call model's predict function and return its results/use them to populate template
    return "some prediction"


if __name__ == "__main__":
    app.run(debug=True)
