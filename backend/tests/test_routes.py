import unittest
from app import create_app
import json

class TestRoutes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()

    def test_predict(self):
        response = self.client.post('/predict', json={
            'level': 75.0,
            'temperature': 22.0,
            'humidity': 45.0
        })
        data = json.loads(response.data)
        self.assertIn('status', data)
        self.assertIn(data['status'], ['full', 'vacio'])

if __name__ == '__main__':
    unittest.main()
