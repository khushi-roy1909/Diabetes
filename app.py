from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

MODEL_ACCURACY = 84.50
model = None
scaler = None
load_error = None

try:
    if os.path.exists("diabetes_model.pkl") and os.path.exists("scaler.pkl"):
        with open("diabetes_model.pkl", "rb") as f:
            model = pickle.load(f)
        with open("scaler.pkl", "rb") as f:
            scaler = pickle.load(f)
    else:
        load_error = "Model files not found. Run train_model.py first."
except Exception as e:
    load_error = f"Error loading model: {e}"


@app.route("/", methods=["GET", "POST"])
def home():
    prediction_text = ""
    probability = None

    if load_error:
        return f"<h2>{load_error}</h2>"

    if request.method == "POST":
        try:
            pregnancies = float(request.form["pregnancies"])
            glucose = float(request.form["glucose"])
            bloodpressure = float(request.form["bloodpressure"])
            skinthickness = float(request.form["skinthickness"])
            insulin = float(request.form["insulin"])
            bmi = float(request.form["bmi"])
            dpf = float(request.form["dpf"])
            age = float(request.form["age"])

            input_data = np.array([[
                pregnancies, glucose, bloodpressure,
                skinthickness, insulin, bmi, dpf, age
            ]])

            scaled_data = scaler.transform(input_data)
            prediction = model.predict(scaled_data)[0]
            probability = round(model.predict_proba(scaled_data)[0][1] * 100, 2)

            if prediction == 1:
                prediction_text = "High chance of Diabetes"
            else:
                prediction_text = "Low chance of Diabetes"

        except Exception as e:
            prediction_text = f"Prediction error: {e}"

    return render_template(
        "index.html",
        prediction_text=prediction_text,
        probability=probability,
        accuracy=MODEL_ACCURACY
    )


if __name__ == "__main__":
    app.run(debug=True)