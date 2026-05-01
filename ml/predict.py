import joblib
import numpy as np

model = joblib.load("ml/model.pkl")

def predict_usage(data):
    X = np.array(data).reshape(-1, 1)
    preds = model.predict(X)
    return float(preds[-1])