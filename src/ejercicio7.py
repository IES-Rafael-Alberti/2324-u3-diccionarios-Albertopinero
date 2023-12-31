'''Ejercicio 3.2.7¶
Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar.
Después se debe mostrar por pantalla la lista de la compra y el coste total,con el siguiente formato'''
def cestaCompra():
    cesta = {}
    continuar = True
    while continuar:
        return continuar
    for item, precio in cesta.items():
        return item,precio
    

if __name__ == "__main__":
    cesta = {}
    continuar = True
    #proceso
    while continuar:
        item = input('Introduce un artículo: ')
        precio = float(input('Introduce el precio de ' + item + ': '))
        cesta[item] = precio
        continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
    coste = 0
    print('Lista de la compra')
    for item, precio in cesta.items():
        print(item,':', precio)
        coste += precio
    #salida
    print('Coste total: ', coste)

