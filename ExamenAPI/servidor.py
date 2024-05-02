from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

# Función para desencriptar la imagen
def decrypt_image(encrypted_img, key):
    cipher_suite = Fernet(key)
    decrypted_image = cipher_suite.decrypt(encrypted_img)
    return decrypted_image

@app.route('/encriptar_imagen', methods=['POST'])
def encriptar_imagen():
    # Recibe la imagen encriptada desde el cliente
    encrypted_img = request.files['imagen'].read()
    
    # Clave de encriptación (debería ser la misma que se usó para encriptar la imagen en el cliente)
    key = request.form['key']
    
    # Desencripta la imagen
    print("Desencriptando imagen...")
    decrypted_img = decrypt_image(encrypted_img, key.encode())
    print("Imagen desencriptada")
    
    # Guarda la imagen desencriptada
    with open("imagen_desencriptada.jpg", "wb") as f:
        f.write(decrypted_img)
    print("Imagen desencriptada guardada como 'imagen_desencriptada.jpg'")
    
    return jsonify({"mensaje": "Imagen desencriptada guardada como 'imagen_desencriptada.jpg'"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  
