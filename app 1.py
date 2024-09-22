import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("rf_model3.pkl", "rb"))

@flask_app.route("/")
def home():
    return render_template("index.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    # Get features from the form
    features = [float(request.form["Age"]), 
                float(request.form["Sex"]), 
                float(request.form["RestingBP"]), 
                float(request.form["Cholesterol"]), 
                float(request.form["FastingBS"]), 
                float(request.form["MaxHR"]), 
                float(request.form["ExerciseAngina"]), 
                float(request.form["Oldpeak"])]

    # Predict
    prediction = model.predict([features])[0]

    # Convert prediction to meaningful output
    if prediction == 0:
        prediction_text = "No Heart Disease"
    else:
        prediction_text = "Heart Disease"

    return render_template("index.html", prediction_text=prediction_text)

if __name__ == "__main__":
    flask_app.run(debug=True)
