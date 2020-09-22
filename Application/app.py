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
model = pickle.load(open("/Users/logno/Documents/Home/BAF1/model.pkl", "rb"))


@app.route("/")
def home():
    # Main page. The line below throws an error and idk why
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
