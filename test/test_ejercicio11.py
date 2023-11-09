from src.ejercicio11 import datosPersonalesClientes

def test_datosPersonalesClientes():
        expected = 1
        resultado = datosPersonalesClientes()
        assert resultado == expected