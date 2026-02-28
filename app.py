# app.py
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# نموذج Linear Regression بسيط: y = 2x + 3
def predict(x):
    return 2 * x + 3

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.get_json()
    x = np.array(data['x'])
    y_pred = predict(x)
    return jsonify({'y_pred': y_pred.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)