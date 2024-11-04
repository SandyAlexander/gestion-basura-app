import joblib
import numpy as np

model_path = 'app/ml/model.pkl'
scaler_path = 'app/ml/scaler.pkl'

try:
    model = joblib.load(model_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Modelo no encontrado en la ruta: {model_path}")
except Exception as e:
    raise RuntimeError(f"Error al cargar el modelo: {e}")

try:
    scaler = joblib.load(scaler_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Escalador no encontrado en la ruta: {scaler_path}")
except Exception as e:
    raise RuntimeError(f"Error al cargar el escalador: {e}")

def predict(features):
    try:
        features = np.array(features).reshape(1, -1)
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)
        return 'full' if prediction[0] == 1 else 'vacio'
    except Exception as e:
        raise RuntimeError(f"Error en la predicción: {e}")
