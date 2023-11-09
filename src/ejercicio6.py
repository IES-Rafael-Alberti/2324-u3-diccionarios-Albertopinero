'''Ejercicio 3.2.6¶
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario.
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''
def datosPersonales():
    datos = {}


if __name__ == "__main__":
    nombre = input("Escribe tu nombre: ")
    edad = input("Escribe tu edad: ")
    direccion = input("Escribe tu dirección: ")
    telefono = input("Escribe tu número de teléfono: ")
    sexo = input("Escribe H o M: ")
    email = input("Escribe tu correo electrónico: ")