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
from sklearn.preprocessing import OneHotEncoder
import datetime as dt
import pickle


app = Flask("Sneaker Price Predictor")
# HACK - commenting out model load since it's not available on github right now
model = pickle.load(open("/Users/logno/Documents/Home/BAF1/model.pkl", "rb"))


@app.route("/")
def home():
    # Main page. The line below throws an error and idk why
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    """
    For rendering results on HTML GUI
    """
    # PREPROCESSING
    features = [x for x in request.form.values()]

    data = pd.DataFrame(
        data=[features],
        columns=[
            "Order_date",
            "Brand",
            "Sneaker_Name",
            "Retail_Price",
            "Release_Date",
            "Shoe_Size",
            "Buyer_Region",
        ],
    )

    # Converting dates into numericals

    data["Order_date"] = pd.to_datetime(data["Order_date"])
    data["Order_date"] = data["Order_date"].map(dt.datetime.toordinal)

    data["Release_Date"] = pd.to_datetime(data["Release_Date"])
    data["Release_Date"] = data["Release_Date"].map(dt.datetime.toordinal)

    object_cols = ["Sneaker_Name", "Buyer_Region", "Brand"]
    # Apply one-hot encoder to each column with categorical data
    OH_encoder = OneHotEncoder(handle_unknown="ignore", sparse=False)
    OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(data[object_cols]))

    # One-hot encoding removed index; put it back
    OH_cols_train.index = data.index

    # Adding the column names after one hot encoding
    OH_cols_train.columns = OH_encoder.get_feature_names(object_cols)

    # Remove categorical columns (will replace with one-hot encoding)
    num_data = data.drop(object_cols, axis=1)

    # Add one-hot encoded columns to numerical features
    bigdata = pd.concat([num_data, OH_cols_train], axis=1)
    bruh = bigdata.columns.to_list()

    return str(bruh)

    # prediction = model.predict(bigdata)

    # output = round(prediction[0], 2)

    # return render_template(
    #     "index.html", prediction_text="Sneaker Price is $ {}".format(output)
    # )


if __name__ == "__main__":
    app.run(debug=True)
