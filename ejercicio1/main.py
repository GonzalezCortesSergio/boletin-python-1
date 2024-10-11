palabras = []

def carga_palabras(fichero):

    palabras = []
    with open (fichero, 'r') as archivo:

        

        for palabra in archivo:
            palabras.append(palabra)

    return palabras


while True:

    print("""
          
          Opción 1: Importar palabras clave
          Opción 2: Mostrar palabras clave
          Opción 0: Salir

          """)
    opc = int(input())

    if (opc == 1):

        palabras = carga_palabras('C:/Users/gonzalez.coser24_tri/Desktop/WORKSPACE/boletin-python-1/ejercicio1/palabras.txt')

        print("Palabras cargadas correctamente")

    if(opc == 2):

        for palabra in palabras[:20]:
            print(palabra)

        

    if(opc == 0):

        break

print("Gracias por utilizar el programa")
