def carga_palabras(fichero):

    palabras = []
    with open (fichero, 'r') as archivo:

        for palabra in archivo:
    
            palabras.append(palabra.strip())

    return palabras

def frecuencia(palabras):

    palabras_frecuencia = dict()

    for palabra in palabras:

        if palabra in palabras_frecuencia:

            palabras_frecuencia[palabra] +=1

        else:
            palabras_frecuencia.update({palabra: 1})

    return palabras_frecuencia


palabras = carga_palabras('C:/Users/gonzalez.coser24_tri/Desktop/WORKSPACE/boletin-python-1/ejercicio2/palabras.txt')

print(frecuencia(palabras))