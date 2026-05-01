from flask import Blueprint, jsonify
from app.services.prediction_service import predict_future

predictions_bp = Blueprint('predictions', __name__)

@predictions_bp.route('/predict')
def predict():
    result = predict_future()
    return jsonify(result)