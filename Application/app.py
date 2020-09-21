import numpy as np
import pandas as pd
from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    redirect,
    render_template_string,
)
import pickle
import cgi
import jinja2
import os


app = Flask("Sneaker Price Predictor", template_folder={"templates"})
model = pickle.load(open("/Users/logno/Documents/Home/BAF1/model.pkl", "rb"))


@app.route("/", methods=["GET"])
def home():
    # Main page. The line below throws an error and idk why
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
