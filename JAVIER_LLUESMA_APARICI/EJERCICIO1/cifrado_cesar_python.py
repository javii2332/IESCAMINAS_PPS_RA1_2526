# cifrado_cesar_python.py

def cifrar_cesar(texto, clave=3):
    """
    Cifra un texto usando el Cifrado César.
    Solo afecta a las letras mayúsculas y minúsculas del alfabeto inglés.
    Otros caracteres (espacios, números, símbolos) se mantienen sin cambios.
    """
    resultado = ""
    for char in texto:
        if 'A' <= char <= 'Z':
            # Manejar mayúsculas
            # Ord es para obtener el valor ASCII del carácter
            # Se resta ord('A') para que 'A' sea 0, 'B' sea 1, etc.
            # Se suma la clave, se aplica módulo 26 para que dé la vuelta (Z -> A)
            # Se suma ord('A') de nuevo para volver al rango ASCII de mayúsculas
            shift = (ord(char) - ord('A') + clave) % 26
            resultado += chr(shift + ord('A'))
        elif 'a' <= char <= 'z':
            # Manejar minúsculas (mismo proceso)
            shift = (ord(char) - ord('a') + clave) % 26
            resultado += chr(shift + ord('a'))
        else:
            # Mantener otros caracteres (espacios, puntuación, etc.)
            resultado += char
    return resultado

def descifrar_cesar(texto_cifrado, clave=3):
    """
    Descifra un texto usando el Cifrado César.
    Es simplemente llamar a cifrar con una clave negativa.
    """
    # En un cifrado por sustitución, descifrar es cifrar con la clave inversa.
    # La clave inversa es 26 - clave, o simplemente -clave.
    return cifrar_cesar(texto_cifrado, -clave)

# --- Ejemplo de Uso ---
if __name__ == "__main__":
    mensaje_original = "Hola Mundo! 2024"
    clave_usada = 3

    texto_cifrado = cifrar_cesar(mensaje_original, clave_usada)
    print(f"Mensaje Original: {mensaje_original}")
    print(f"Clave Utilizada:  {clave_usada}")
    print(f"Mensaje Cifrado:  {texto_cifrado}")

    texto_descifrado = descifrar_cesar(texto_cifrado, clave_usada)
    print(f"Mensaje Descifrado: {texto_descifrado}")

    # Comprobación de que el descifrado es igual al original
    assert mensaje_original == texto_descifrado
