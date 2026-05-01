def predict_future():
    data = [10, 20, 30]  # example
    current = 50         # example

    prediction = predict_usage(data)

    # FIX HERE 👇
    if isinstance(prediction, list):
        prediction = prediction[0]

    prediction = (prediction + current) / 2

    return {"prediction": prediction}
