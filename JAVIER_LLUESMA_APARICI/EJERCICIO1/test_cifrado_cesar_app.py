# test_cifrado_cesar_app.py

import unittest
from cifrado_cesar_python import cifrar_cesar, descifrar_cesar

class TestCesarCipher(unittest.TestCase):

    # PRUEBA UNITARIA 1: Cifrado y Descifrado Básico
    def test_01_cifrado_descifrado_basico(self):
        """Prueba que un texto simple se cifra y descifra correctamente."""
        texto_original = "PYTHON"
        clave = 3
        texto_cifrado_esperado = "SBWKRQ"

        cifrado = cifrar_cesar(texto_original, clave)
        self.assertEqual(cifrado, texto_cifrado_esperado, "El cifrado básico falló")

        descifrado = descifrar_cesar(cifrado, clave)
        self.assertEqual(descifrado, texto_original, "El descifrado básico falló")

    # PRUEBA UNITARIA 2: Manejo de Mayúsculas, Minúsculas y Espacios
    def test_02_manejo_de_casos_y_espacios(self):
        """Prueba el manejo de mayúsculas, minúsculas y caracteres no alfabéticos."""
        texto_original = "Cyber Seguridad"
        clave = 5
        texto_cifrado_esperado = "Hdgjw Xjlzwnifi"

        cifrado = cifrar_cesar(texto_original, clave)
        self.assertEqual(cifrado, texto_cifrado_esperado, "El manejo de casos y espacios falló")

    # PRUEBA UNITARIA 3: El Efecto 'Wrap-Around' (Z a A)
    def test_03_efecto_wrap_around(self):
        """Prueba que el cifrado dé la vuelta de Z a A y de z a a."""
        texto_original = "XYZxyz"
        clave = 3
        # X+3=A, Y+3=B, Z+3=C
        texto_cifrado_esperado = "ABCabc"

        cifrado = cifrar_cesar(texto_original, clave)
        self.assertEqual(cifrado, texto_cifrado_esperado, "El wrap-around de Z a A falló")

    # PRUEBA UNITARIA 4: Caracteres Especiales y Clave Cero
    def test_04_caracteres_especiales_y_clave_cero(self):
        """Prueba que los números y símbolos se mantienen, y que la clave 0 no cambia nada."""
        texto_original = "Cibersec2024!"
        clave_cero = 0

        cifrado = cifrar_cesar(texto_original, clave_cero)
        # Con clave 0, el texto cifrado debe ser idéntico al original
        self.assertEqual(cifrado, texto_original, "La clave 0 falló")

        # Prueba de que los caracteres especiales se mantienen con clave 3
        texto_original_2 = "Test!@#"
        clave = 3
        texto_cifrado_2 = cifrar_cesar(texto_original_2, clave)
        self.assertEqual(texto_cifrado_2, "Whvw!@#", "El manejo de símbolos falló")

if __name__ == '__main__':
    # Ejecuta todas las pruebas en la clase TestCesarCipher
    unittest.main()
