from ml.predict import predict_usage

def predict_future():
    data = [10, 20, 30]   # example
    current = 50          # example

    prediction = predict_usage(data)

    prediction = (prediction + current) / 2

    return {"prediction": prediction}
