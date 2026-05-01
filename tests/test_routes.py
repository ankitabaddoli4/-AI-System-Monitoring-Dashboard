import unittest
from run import app

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_metrics(self):
        response = self.client.get('/metrics')
        self.assertEqual(response.status_code, 200)

    def test_prediction(self):
        response = self.client.get('/predict')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()