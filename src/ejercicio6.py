'''Ejercicio 3.2.6¶
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''
def datosPersonales():
    persona = {}
    continuar = True
    while continuar:
        return persona

if __name__ == "__main__":
    persona = {}
    continuar = True
    while continuar:
        clave = input('¿Qué dato quieres introducir? ')
        valor = input(clave + ': ')
        persona[clave] = valor
        print(persona)