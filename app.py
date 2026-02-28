from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)    


def predict(x):
    return 2 * x + 3

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.get_json()
    x = np.array(data['x'])
    y_pred = predict(x)
    return jsonify({'y_pred': y_pred.tolist()})

@app.route('/')
def home():
    return "Linear Regression API is running! Use POST /predict."
