import unittest
from app.services.monitor_service import get_system_metrics

class TestServices(unittest.TestCase):

    def test_metrics_data(self):
        data = get_system_metrics()
        self.assertIn('cpu', data)
        self.assertIn('memory', data)

if __name__ == "__main__":
    unittest.main()