import pytest
from src.ejercicio4 import formatoFecha

@pytest.mark.parametrize(
    "fecha,mensaje",
    [
        ("25/6/2004","25 de junio de 2004")
    ]
    )

def test_formatoFecha(fecha,mensaje):
    assert formatoFecha(fecha) == mensaje