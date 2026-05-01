from flask import Blueprint, jsonify
from app.services.alert_service import check_alert

alerts_bp = Blueprint('alerts', __name__)

@alerts_bp.route('/alert')
def alert():
    result = check_alert()
    return jsonify(result)