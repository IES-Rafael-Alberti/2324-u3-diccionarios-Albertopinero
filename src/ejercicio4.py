'''Ejercicio 3.2.4¶
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y
muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.'''
def formatoFecha(fecha):
    meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
    fecha = input("Escribe la fecha en formato dd/mm/aaaa")
    fecha = fecha.split('/')
    mensaje = (fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])
    return mensaje
    
if __name__ == "__main__":
    meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
    #entrada
    fecha = input("Escribe la fecha en formato dd/mm/aaaa: ")
    #proceso
    fecha = fecha.split('/')
    mensaje = formatoFecha(fecha)
    #salida
    print(mensaje)
    