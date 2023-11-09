persona = {}
clave = input('¿Qué dato quieres introducir? ')
while clave != "salir":
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    otroDato = input("¿Qué otro dato quieres introducir?: ")
    (clave)