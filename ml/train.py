import numpy as np
import joblib
from ml.model import CPUUsageModel

# realistic CPU-like pattern
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([30, 40, 35, 50, 45])

model = CPUUsageModel()
model.train(X, y)

joblib.dump(model, "ml/model.pkl")

print("Model trained!")