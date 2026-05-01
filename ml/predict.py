import joblib

model = None

def load_model():
    global model
    if model is None:
        try:
            model = joblib.load("ml/model.pkl")
        except Exception:
            model = None
    return model


def predict_usage(data):
    model = load_model()

    if model:
        result = model.predict([data])
        return result[0]   # always return number
    else:
        return sum(data) / len(data)  # fallback
