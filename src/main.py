# 1. Definir la aplicación y asignarla a una variable (ej: 'main')
from flask import Flask


main = Flask(__name__)

def login_socio(email, password):
    # Aquí iría la lógica para verificar el login del socio
    # Por simplicidad, asumimos que la función retorna True si el login es exitoso
    if email == "gustavo@example.com" and password == "correctpassword":
        return True
    return False

if __name__ == "__main__":
    main.run(debug=True)