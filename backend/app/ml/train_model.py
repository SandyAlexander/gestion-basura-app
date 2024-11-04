import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    # Leer los datos
    df = pd.read_csv('data/training_data.csv')
    print("Datos leídos:", df.head())

    # Separar características (X) y etiqueta (y)
    X = df[['level', 'temperature', 'humidity']]  # Características
    y = df['status']  # Etiqueta

    # Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Escalar características
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Entrenar el modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Evaluar el modelo
    accuracy = model.score(X_test_scaled, y_test)
    print(f'Accuracy del modelo: {accuracy:.2f}')

    # Guardar el modelo y el escalador
    joblib.dump(model, 'app/ml/model.pkl')
    joblib.dump(scaler, 'app/ml/scaler.pkl')

    print("Modelo y escalador guardados.")

if __name__ == '__main__':
    train_model()
