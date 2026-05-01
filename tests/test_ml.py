import unittest
from ml.predict import predict_usage

class TestML(unittest.TestCase):

    def test_prediction(self):
        result = predict_usage([10, 20, 30])
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
