def traduccionPalabras(palabras):
    diccionario = {}
    for i in palabras.split(','):
        return i
    for i in frase.split():
        if i in diccionario:
            return i
        return i

if __name__ == "__main__":
    diccionario = {}
    #entrada
    palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
    #proceso
    for i in palabras.split(','):
        clave, valor = i.split(':')
        diccionario[clave] = valor
    frase = input('Introduce una frase en español: ')
    for i in frase.split():
        if i in diccionario:
    #salida
            print(diccionario[i], end=' ')
        else:
            print(i, end=' ')
