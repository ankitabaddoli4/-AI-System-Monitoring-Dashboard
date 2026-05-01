def predict_usage(data):
    model = load_model()

    if model:
        result = model.predict([data])
        return result[0]   # ✅ always return number
    else:
        return sum(data) / len(data)
