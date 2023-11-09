'''Ejercicio 3.2.3¶
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.'''
def kilosFrutas(fruta,frutas):
    if frutas in fruta:
        return frutas
    
if __name__ == "__main__":
    frutas = {'Platano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
    fruta = input("¿Qué fruta deseas comprar?(Plátano, Manzana, Pera, Naranja): ").title()
    kilos = float(input("¿Cuántos Kilos deseas comprar?: "))
    if fruta in frutas:
        print(kilos, 'kilos de', fruta, 'cuestan', frutas[fruta]*kilos, '€')
    else:
        print("Error, esta fruta se ha agotado, lo sentimos")
    resultado = kilosFrutas(fruta,frutas)