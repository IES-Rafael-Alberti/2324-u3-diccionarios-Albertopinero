from src.ejercicio5 import notasCurso

def test_notasCurso():
    curso = ["Matemáticas", "Física", "Química"]
    resultado = [6, 4, 5]
    output = notasCurso(curso, resultado)
    assert len(output) == 2