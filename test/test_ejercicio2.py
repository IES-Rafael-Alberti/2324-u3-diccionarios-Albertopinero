import pytest
from src.ejercicio2 import datosPersonales

@pytest.mark.parametrize(
    "nombre,edad,direccion,telefono,mensaje",
    [
        ("Alberto",19,"C/Manga de Villaluenga","601126714","Alberto tiene 19 años, vive en C/Manga de Villaluenga y su número de teléfono es 601126714")
    ]
    )

def test_datosPersonales(nombre,edad,direccion,telefono,mensaje):
    assert datosPersonales(nombre,edad,direccion,telefono) == mensaje