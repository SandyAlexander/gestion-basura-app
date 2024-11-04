import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Parámetros de simulación
num_containers = 10
num_samples_per_container = 20
start_date = datetime(2024, 1, 1)

# Crear directorio si no existe
if not os.path.exists('data'):
    os.makedirs('data')

# Simular datos
data = []
for container_id in range(1, num_containers + 1):
    for sample in range(num_samples_per_container):
        timestamp = start_date + timedelta(minutes=sample * 10)
        level = np.random.uniform(0, 100)  # Nivel de llenado simulado
        temperature = np.random.uniform(5, 35)  # Temperatura simulada
        humidity = np.random.uniform(10, 90)  # Humedad simulada
        status = 'full' if level > 80 else 'empty'  # Etiqueta basada en el nivel de llenado

        data.append({
            'container_id': container_id,
            'timestamp': timestamp,
            'level': level,
            'temperature': temperature,
            'humidity': humidity,
            'status': status
        })

# Crear DataFrame
df = pd.DataFrame(data)

# Convertir la columna de timestamp a una representación numérica si es necesario
# En este caso, eliminaremos la columna de timestamp ya que no es numérica
df['timestamp'] = pd.to_datetime(df['timestamp']).astype(int) / 10**9  # Convertir a timestamp en segundos

# Eliminar columnas que no son necesarias para el entrenamiento
df = df[['container_id', 'level', 'temperature', 'humidity', 'status']]

# Convertir las etiquetas de estado en valores numéricos
df['status'] = df['status'].map({'full': 1, 'empty': 0})

# Guardar el DataFrame en un archivo CSV
df.to_csv('data/training_data.csv', index=False)

print("Archivo 'data/training_data.csv' creado con datos simulados.")
