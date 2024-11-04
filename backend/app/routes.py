from flask import Blueprint, request, jsonify
from app.ml.predictor import predict

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/containers', methods=['GET'])
def get_containers():
    containers = [
        {"id": 1, "name": "Container 1", "latitude": -0.446850, "longitude": -76.998753, "level": 10, "temperature": 25, "humidity": 65},
        {"id": 2, "name": "Container 2", "latitude": -0.458218,  "longitude": -76.992904, "level": 90, "temperature": 50, "humidity": 50},
        {"id": 3, "name": "Container 3", "latitude": -0.467981,   "longitude": -76.987797, "level": 15, "temperature": 10, "humidity": 68},
        {"id": 4, "name": "Container 4", "latitude": -0.443542,  "longitude": -77.000414,  "level": 80, "temperature": 70, "humidity": 70},

        # Agrega más contenedores aquí
    ]
    return jsonify(containers)

@api_bp.route('/api/predict', methods=['POST'])
def get_prediction():
    data = request.json
    print("Received data:", data)  # Añadir este print para depuración
    if not data or 'level' not in data or 'temperature' not in data or 'humidity' not in data:
        return jsonify({'error': 'Missing data'}), 400

    features = [data['level'], data['temperature'], data['humidity']]
    prediction = predict(features)
    return jsonify({'status': prediction})
