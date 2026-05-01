from flask import jsonify
from app.services.prediction_service import predict_future

def predict():
    try:
        result = predict_future()
        return jsonify(result), 200
    except Exception:
        return jsonify({"error": "Prediction failed"}), 500
