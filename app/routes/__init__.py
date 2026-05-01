from .metrics import metrics_bp
from .predictions import predictions_bp
from .alerts import alerts_bp
from .main import main_bp

def register_routes(app):
    app.register_blueprint(metrics_bp)
    app.register_blueprint(predictions_bp)
    app.register_blueprint(alerts_bp)
    app.register_blueprint(main_bp)   # 👈 add this
