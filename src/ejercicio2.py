'''Ejercicio 3.2.2¶
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.'''
import time
def datosPersonales(nombre,edad,direccion,telefono):
    datos = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
    mensaje = datos['nombre']+' tiene '+str(datos['edad'])+' años, vive en '+datos['direccion']+' y su número de teléfono es '+datos['telefono']
    return mensaje
if __name__ == "__main__":
    nombre = input("Escribe tu nombre: ")
    edad = int(input("Escribe tu edad: "))
    direccion = input("Escribe tu dirección: ")
    telefono = input("Escribe tu número de teléfono: ")
    print("Procesando datos...")
    time.sleep(2)
    mensaje=datosPersonales(nombre,edad,direccion,telefono)
    print(mensaje)
