import pytest
from src.ejercicio3 import kilosFrutas

@pytest.mark.parametrize(
    "fruta,frutas,resultado",
    [
        ({'Platano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70},"Platano",1.35),
        ({'Platano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70},"Manzana",0.80),
        ({'Platano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70},"Pera",0.85),
        ({'Platano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70},"Naranja",0.70)
    ]
    )

def test_kilosFrutas(fruta,frutas,resultado):
    assert kilosFrutas(fruta,frutas),4 == resultado