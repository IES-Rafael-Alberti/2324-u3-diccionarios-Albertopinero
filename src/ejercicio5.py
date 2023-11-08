'''Ejercicio 3.2.5¶
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5}
y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos.
Al final debe mostrar también el número total de créditos del curso.'''
def notasCurso(curso,resultado):
    curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    for asignatura, creditos in curso.items():
        return asignatura, creditos

    

if __name__ == "__main__":
    curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    #proceso
    total_creditos = 0
    for asignatura, creditos in curso.items():
        print(asignatura, 'tiene', creditos, 'créditos')
        total_creditos += creditos
        mensaje = 'Número total de créditos del curso: ' + str(total_creditos)
    #salida
    resultado = notasCurso(curso)