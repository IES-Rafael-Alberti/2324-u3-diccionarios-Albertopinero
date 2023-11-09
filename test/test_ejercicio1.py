import pytest
from src.ejercicio1 import monedasInternacionales

@pytest.mark.parametrize(
    "divisas,moneda,resultado",
    [
        ({'euro':'€', 'dollar':'$', 'yen':'¥'},"euro","€"),
        ({'euro':'€', 'dollar':'$', 'yen':'¥'},"dollar","$"),
        ({'euro':'€', 'dollar':'$', 'yen':'¥'},"yen","¥")
    ]
)

def test_monedasInternacionales(divisas,moneda,resultado):
    assert monedasInternacionales(divisas,moneda),3 == resultado