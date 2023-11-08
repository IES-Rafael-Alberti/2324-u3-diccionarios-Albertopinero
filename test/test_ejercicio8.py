from src.ejercicio8 import traduccionPalabras

def test_traduccionPalabras():
    palabras = "hola:hello"
    resultado = traduccionPalabras(palabras)
    assert resultado == "hola:hello"