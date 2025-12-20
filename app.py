# app.py

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the trained model
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'model.pkl')

with open(model_path, 'rb') as file:
    model = pickle.load(file)



with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [
        float(request.form['IQ']),
        float(request.form['Prev_Sem_Result']),
        float(request.form['CGPA']),
        float(request.form['Academic_Performance']),
        float(request.form['Internship_Experience']),
        float(request.form['Extra_Curricular_Score']),
        float(request.form['Communication_Skills']),
        float(request.form['Projects_Completed'])
    ]

    final_features = np.array([features])
    prediction = model.predict(final_features)[0]

    output = 'Placed' if prediction == 1 else 'Not Placed'

    return render_template(
        'index.html',
        prediction_text=f'Prediction: {output}'
    )


if __name__ == "__main__":
    app.run(debug=True)