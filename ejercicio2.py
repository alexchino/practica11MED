#Crea un módulo llamado "generador_contraseñas" que genere contraseñas aleatorias. La
#función debe aceptar un argumento: la longitud de la contraseña. La contraseña generada
#debe ser una combinación de letras mayúsculas, letras minúsculas y números.

import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = []

    for i in range(length):
        password.append(secrets.choice(characters))

    return ''.join(password)

# Prueba la función generate_password
print(generate_password(12))