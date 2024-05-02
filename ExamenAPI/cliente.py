import requests
from cryptography.fernet import Fernet

# Función para encriptar la imagen
def encrypt_image(image_path, key):
    with open(image_path, 'rb') as f:
        img = f.read()
    cipher_suite = Fernet(key)
    encrypted_image = cipher_suite.encrypt(img)
    return encrypted_image

# Parámetros del cliente
image_path = "imagen.jpg"  # Ruta de la imagen a enviar
key = Fernet.generate_key()  # Clave de encriptación

# Encripta la imagen
print("Encriptando imagen...")
encrypted_image = encrypt_image(image_path, key)
print("Imagen encriptada guardada como 'imagen_encriptada.jpg'")

# Guarda la imagen encriptada
with open("imagen_encriptada.jpg", "wb") as f:
    f.write(encrypted_image)

# Envía la imagen encriptada al servidor
print("Enviando imagen encriptada al servidor...")
url = 'http://127.0.0.1:5001/encriptar_imagen'  # Cambia el puerto a 5001
files = {'imagen': ('imagen_encriptada.jpg', encrypted_image)}
response = requests.post(url, files=files, data={'key': key.decode()})
print("Imagen encriptada enviada")

print(response.json())
