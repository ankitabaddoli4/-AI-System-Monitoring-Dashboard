import joblib

model = None

def load_model():
    global model
    if model is None:
        try:
            model = joblib.load("ml/model.pkl")
        except Exception:
            model = None  # prevent crash
    return model

def predict_usage(data):
    model = load_model()

    if model:
        return model.predict([data])  # ensure 2D input
    else:
        return [sum(data) / len(data)]  # simple fallback
