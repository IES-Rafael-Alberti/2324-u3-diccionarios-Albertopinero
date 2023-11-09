from src.ejercicio10 import baseDeDatos

def test_baseDeDatos():
        def baseDeDatos():
            return {}
        result = baseDeDatos()
        assert isinstance(result, dict)