from src.ejercicio4 import formatoFecha

def test_formatoFecha():
    from unittest.mock import patch

    with patch('builtins.input', return_value='01/01/2022'):
        assert formatoFecha('01/01/2022') == ('01', 'de', 'enero', 'de', '2022')

    with patch('builtins.input', return_value='31/12/2022'):
        assert formatoFecha('31/12/2022') == ('31', 'de', 'diciembre', 'de', '2022')

    with patch('builtins.input', return_value='15/06/2023'):
        assert formatoFecha('15/06/2023') == ('15', 'de', 'junio', 'de', '2023')