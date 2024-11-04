from app import create_app

# Crea una instancia de la aplicación Flask
app = create_app()

if __name__ == "__main__":
    # Ejecuta la aplicación en el modo de desarrollo
    app.run(
        host='0.0.0.0',  # Permite conexiones desde cualquier IP
        port=5000,       # Puerto en el que se ejecutará la aplicación
        debug=True       # Activa el modo de depuración
    )
