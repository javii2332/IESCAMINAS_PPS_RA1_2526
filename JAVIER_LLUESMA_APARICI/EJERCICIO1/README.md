## README.md (Aplicación Python)

Este `README.md` documenta la aplicación de cifrado César y el proceso para ejecutar sus 4 pruebas unitarias.

```markdown
# Aplicación de Criptografía (Cifrado César) y Pruebas Unitarias

## Descripción

Este repositorio contiene una aplicación básica en Python que implementa el **Cifrado César**, un método criptográfico de sustitución sencillo. La aplicación consta de dos funciones principales: `cifrar_cesar` y `descifrar_cesar`.

Además, se incluyen **4 pruebas unitarias** utilizando el módulo estándar `unittest` de Python para asegurar la correcta funcionalidad del cifrado en diferentes escenarios.

## Estructura de Archivos

* `cifrado_cesar_python.py`: Contiene las funciones de cifrado y descifrado.
* `test_cifrado_cesar_app.py`: Contiene la clase `TestCesarCipher` con las 4 pruebas unitarias.

## Pre-requisitos

* **Python 3.x** instalado en el sistema.

## 1. Archivo: `cifrado_cesar_python.py`

Guardar el siguiente código como `cifrado_cesar_python.py`:

```python
def cifrar_cesar(texto, clave=3):
    resultado = ""
    for char in texto:
        if 'A' <= char <= 'Z':
            shift = (ord(char) - ord('A') + clave) % 26
            resultado += chr(shift + ord('A'))
        elif 'a' <= char <= 'z':
            shift = (ord(char) - ord('a') + clave) % 26
            resultado += chr(shift + ord('a'))
        else:
            resultado += char
    return resultado

def descifrar_cesar(texto_cifrado, clave=3):
    return cifrar_cesar(texto_cifrado, -clave)

if __name__ == "__main__":
    mensaje_original = "Hola Mundo! 2024"
    texto_cifrado = cifrar_cesar(mensaje_original, 3)
    texto_descifrado = descifrar_cesar(texto_cifrado, 3)
    print(f"Original: {mensaje_original}\nCifrado: {texto_cifrado}\nDescifrado: {texto_descifrado}")

2. Archivo: test_cifrado_cesar_app.py (Pruebas Unitarias)
Guarda el siguiente código como test_cifrado_cesar_app.py:

Python

import unittest
from cifrado_cesar_python import cifrar_cesar, descifrar_cesar

class TestCesarCipher(unittest.TestCase):

    # PRUEBA 1: Cifrado y Descifrado Básico
    def test_01_cifrado_descifrado_basico(self):
        texto_original = "PYTHON"
        clave = 3
        texto_cifrado_esperado = "SBWKRQ"
        self.assertEqual(cifrar_cesar(texto_original, clave), texto_cifrado_esperado)
        self.assertEqual(descifrar_cesar(texto_cifrado_esperado, clave), texto_original)

    # PRUEBA 2: Manejo de Mayúsculas, Minúsculas y Espacios
    def test_02_manejo_de_casos_y_espacios(self):
        texto_original = "Cyber Seguridad"
        clave = 5
        texto_cifrado_esperado = "Hdgjw Xjluxwnief"
        self.assertEqual(cifrar_cesar(texto_original, clave), texto_cifrado_esperado)

    # PRUEBA 3: El Efecto 'Wrap-Around' (Z a A)
    def test_03_efecto_wrap_around(self):
        texto_original = "XYZxyz"
        clave = 3
        texto_cifrado_esperado = "ABCabc"
        self.assertEqual(cifrar_cesar(texto_original, clave), texto_cifrado_esperado)

    # PRUEBA 4: Caracteres Especiales y Clave Cero
    def test_04_caracteres_especiales_y_clave_cero(self):
        texto_original = "Cibersec2024!"
        clave_cero = 0
        self.assertEqual(cifrar_cesar(texto_original, clave_cero), texto_original)
        
        texto_original_2 = "Test!@#"
        clave = 3
        self.assertEqual(cifrar_cesar(texto_original_2, clave), "Whvw!@#")

if __name__ == '__main__':
    unittest.main()

3. Ejecución de las Pruebas
Asegúrate de que ambos archivos (cifrado_cesar_python.py y test_cifrado_cesar_app.py) estén en la misma carpeta.

Ejecuta el archivo de pruebas desde la terminal:

Bash

python3 test_cifrado_cesar_app.py

Resultado Esperado
Si las 4 pruebas pasan con éxito, la salida será similar a:

....
----------------------------------------------------------------------
Ran 4 tests in 0.0xx s

OK
