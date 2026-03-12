import joblib
from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

model = joblib.load('Heart_attack_prediction.pkl')

FEATURE_MINS = [29,  0,  0,  94, 126, 0,  0,   71, 0,  0.0, 0,  0,  0]
FEATURE_MAXS = [77,  1,  3, 200, 564, 1,  2,  202, 1,  6.2, 2,  4,  3]

def minmax_normalize(raw_values):
    """Normalize raw input values to 0-1 range, matching training-time scaling."""
    normed = []
    for i, v in enumerate(raw_values):
        rng = FEATURE_MAXS[i] - FEATURE_MINS[i]
        n = (v - FEATURE_MINS[i]) / rng if rng != 0 else 0.0
        n = max(0.0, min(1.0, n))   # clamp to valid range
        normed.append(n)
    return normed


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Step 1: Read raw values from frontend
    raw_features = [
        float(data['age']),
        float(data['sex']),
        float(data['cp']),
        float(data['trestbps']),
        float(data['chol']),
        float(data['fbs']),
        float(data['restecg']),
        float(data['thalach']),
        float(data['exang']),
        float(data['oldpeak']),
        float(data['slope']),
        float(data['ca']),
        float(data['thal'])
    ]

    # Step 2: Normalize - THIS IS THE KEY FIX
    # Without this, the model receives e.g. age=63 instead of 0.708,
    # giving completely wrong extreme probabilities (0% or 100%).
    normalized = minmax_normalize(raw_features)
    features = np.array(normalized).reshape(1, -1)

    # Step 3: Predict
    prediction  = model.predict(features)[0]
    probability = model.predict_proba(features)[0]
    # predict_proba returns [prob_class_0, prob_class_1] in range 0.0-1.0
    # class 0 = No Heart Attack, class 1 = Heart Attack

    # Step 4: Multiply by 100 ONCE to get percentage
    prob_no  = round(float(probability[0]) * 100, 2)   # e.g. 38.50
    prob_yes = round(float(probability[1]) * 100, 2)   # e.g. 61.50

    result = "High Risk of Heart Attack" if prediction == 1 else "Low Risk of Heart Attack"

    return jsonify({
        "prediction": result,
        "prob_yes":   prob_yes,    # already a % value e.g. 61.50
        "prob_no":    prob_no,     # already a % value e.g. 38.50
    })


if __name__ == "__main__":
    app.run(debug=True)
