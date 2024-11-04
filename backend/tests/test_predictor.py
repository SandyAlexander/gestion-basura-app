import unittest
from app.ml.predictor import predict

class TestPredictor(unittest.TestCase):
    def test_predict(self):
        features = [75.0, 22.0, 45.0]
        result = predict(features)
        self.assertIn(result, ['full', 'vacio'])

if __name__ == '__main__':
    unittest.main()
