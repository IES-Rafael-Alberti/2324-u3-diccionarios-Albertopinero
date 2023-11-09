'''Ejercicio 3.2.1¶
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.'''
def monedasInternacionales(divisas,moneda):
    if moneda == "euro":
        return moneda
    elif moneda == "dollar":
        return moneda
    elif moneda == "yen":
        return moneda


if __name__ == "__main__":
    divisas = {'euro':'€', 'dollar':'$', 'yen':'¥'}
    #entrada
    moneda = input("Escribe la divisa para ver su símbolo(Euro, Dollar, Yen): ").lower()
    #proceso
    if moneda == "euro":
        print("El símbolo del Euro es €")
    elif moneda == "dollar":
        print("El símbolo del Dollar es $")
    elif moneda == "yen":
        print("El símbolo del Yen es ¥")
    else:
    #salida
        print("Esta divisa no está en el diccionario")
    resultado = monedasInternacionales(divisas,moneda)