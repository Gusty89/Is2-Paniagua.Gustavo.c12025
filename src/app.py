from flask import Flask
from src.controller.libro_controller import libro_bp

app = Flask(__name__)

# Registrar Blueprint
app.register_blueprint(libro_bp, url_prefix="/libros")

@app.route("/")
def home():
    return "📚 API de Biblioteca en Python corriendo correctamente"

if __name__ == "__main__":
    app.run(debug=True)
