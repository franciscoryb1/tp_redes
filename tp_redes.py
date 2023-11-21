import requests,zipfile, io, csv,json
#Intento la descarga del archivo binario
url= 'https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json'
filename = 'file.json'
r = requests.get (url)

r.json()
json_str = json.dumps(r.json())

with open(filename, 'w') as f:
    f.write(r.text)


# Cargar el archivo JSON
with open(filename) as file:
    datos = json.load(file)

# prueba
# print(datos[0]['country'])

# buscar libros posteriores a un año
def buscar_libros_posterior_anio(libros, anio_buscado):

    libros_encontrados = [libro for libro in libros if libro["year"] > anio_buscado]
    return libros_encontrados


anio_buscado = 1950
resultados = buscar_libros_posterior_anio(datos, anio_buscado)

print(f"Libros publicados después de {anio_buscado}:")
for libro in resultados:
    print(libro['title'])

print('----------------------------------------------------------------------------')

# buscar libros entre dos años
def buscar_libros_entre_anios(libros, anio_inicio, anio_fin):
 
    libros_encontrados = [
        libro for libro in libros if anio_inicio <= libro["year"] <= anio_fin
    ]
    return libros_encontrados


# anio_inicio = 1950
# anio_fin = 1960

# resultados = buscar_libros_entre_anios(datos, anio_inicio, anio_fin)

# print(f"Libros publicados entre {anio_inicio} y {anio_fin}:")
# for libro in resultados:
#     print(libro['title'])




def buscar_libros_menores_anio(libros, anio_buscado):

    libros_encontrados = [libro for libro in libros if libro["year"] < anio_buscado]
    return libros_encontrados



def buscar_libros_por_autor(libros, autor):

    libros_encontrados = [libro for libro in libros if autor.lower() in libro["author"].lower()]
    return libros_encontrados


def buscar_libros_pais(libros, pais):

    libros_encontrados = [libro for libro in libros if pais.lower() in libro["country"].lower()]
    return libros_encontrados

# print('Libros argentina: ')
# print(buscar_libros_pais(datos, 'arg'))


def buscar_libros_por_title(libros, titulo):

    libros_encontrados = [libro for libro in libros if titulo.lower() in libro["title"].lower()]
    return libros_encontrados


def buscar_libros_por_lenguaje(libros, lenguage):

    libros_encontrados = [libro for libro in libros if lenguage.lower() in libro["lenguage"].lower()]
    return libros_encontrados


# buscar libros menpres a tal pagina
def buscar_libros_menores_pagina(libros, pages):

    libros_encontrados = [libro for libro in libros if libro["pages"] > pages]
    return libros_encontrados


anio_buscado = 300
resultados = buscar_libros_posterior_anio(datos, anio_buscado)

print(f"Libros publicados después de {anio_buscado}:")
for libro in resultados:
    print(libro['title'])

print('----------------------------------------------------------------------------')

# buscar libros entre dos años
def libros_encontrados_entre_paginas(libros, pag_desde, pag_hasta):
 
    libros_encontrados = [
        libro for libro in libros if pag_desde <= libro["pages"] <= pag_hasta]
    return libros_encontrados
