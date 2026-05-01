from flask import Blueprint, jsonify
from app.services.monitor_service import get_system_metrics

metrics_bp = Blueprint('metrics', __name__)

@metrics_bp.route('/metrics')
def metrics():
    data = get_system_metrics()
    return jsonify(data)