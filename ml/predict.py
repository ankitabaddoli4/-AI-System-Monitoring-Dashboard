import joblib

model = None

def load_model():
    global model
    if model is None:
        model = joblib.load("ml/model.pkl")
    return model

def predict_usage(data):
    model = load_model()
    return model.predict(data)
