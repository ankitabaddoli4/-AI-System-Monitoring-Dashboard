from ml.predict import predict_usage
from app.services.monitor_service import get_system_metrics

def predict_future():
    current = get_system_metrics()["cpu"]

    # better input pattern
    data = [current * 0.8, current, current * 1.1]

    prediction = predict_usage(data)

    # smooth prediction
    prediction = (prediction + current) / 2

    # clamp safely
    prediction = max(0, min(100, prediction))

    return {
        "predicted_cpu": round(prediction, 2)
    }