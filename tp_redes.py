import requests,zipfile, io, csv,json
#Intento la descarga del archivo binario
url= 'https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json'
filename = 'file.json'
r = requests.get (url)

# Cargar el JSON desde el archivo
# ruta_del_json = "/file.json"  # Reemplaza con la ruta correcta
# with open(ruta_del_json, 'r') as file:
#     libros_json = json.load(file)

r.json()
json_str = json.dumps(r.json())

with open(filename, 'w') as f:
    f.write(r.text)


# Cargar el archivo JSON
with open(filename) as file:
    libro = json.load(file)


# buscar libros en un año puntual
def buscar_libros_igual_anio(libros, anio_buscado):
    libros_encontrados = [libro for libro in libros if libro["year"] == anio_buscado]
    return libros_encontrados

# buscar libros anteriores a un determinado año
def buscar_libros_menores_anio(libros, anio_buscado):
    libros_encontrados = [libro for libro in libros if libro["year"] < anio_buscado]
    return libros_encontrados

# buscar libros posteriores a un determinado año
def buscar_libros_posterior_anio(libros, anio_buscado):
    libros_encontrados = [libro for libro in libros if libro["year"] > anio_buscado]
    return libros_encontrados

# buscar libros entre dos años
def buscar_libros_entre_anios(libros, anio_inicio, anio_fin):
    libros_encontrados = [
        libro for libro in libros if int(anio_inicio) <= int(libro["year"]) <= int(anio_fin)]
    return libros_encontrados


# buscar libro por autor
def buscar_libros_por_author(libros, author):

    libros_encontrados = [libro for libro in libros if author.lower() in libro["author"].lower()]
    return libros_encontrados

# buscar libro por pais
def buscar_libros_country(libros, country):

    libros_encontrados = [libro for libro in libros if country.lower() in libro["country"].lower()]
    return libros_encontrados


# buscar libro por titulo
# def buscar_libros_por_title(libros, title):
#     libros_encontrados = [libro for libro in libros if title.lower() in libro["title"].lower()]
#     return libros_encontrados

def buscar_libros_por_title(libros, title):
    indices_y_libros = {i: libro for i, libro in enumerate(libros) if title.lower() in libro["title"].lower()}
    return indices_y_libros

# buscar libro por lenguaje
def buscar_libros_por_lenguaje(libros, lenguage):

    libros_encontrados = [libro for libro in libros if lenguage.lower() in libro["lenguage"].lower()]
    return libros_encontrados


# buscar libros con un numero de paginas especifico
def buscar_libros_pages(libros, pages):
    libros_encontrados = [libro for libro in libros if int(libro["pages"]) == int(pages)]
    return libros_encontrados

# buscar libros mcon menos paginas que n
def buscar_libros_menores_page(libros, pages):
    libros_encontrados = [libro for libro in libros if int(libro["pages"]) > int(pages)]
    return libros_encontrados

# buscar libros con mas paginas que n
def buscar_libros_mayores_page(libros, pages):
    libros_encontrados = [libro for libro in libros if int(libro["pages"]) > int(pages)]
    return libros_encontrados

# buscar libros con paginas entre n y m
def buscar_libros_entre_pages(libros, pag_desde, pag_hasta):
    libros_encontrados = [libro for libro in libros if int(pag_desde) <= int(libro["pages"]) <= int(pag_hasta)]
    return libros_encontrados

# Borrar un libro
def borrar(libros, indices_eliminar):
    for indice in sorted(indices_eliminar, reverse=True):
        libros.pop(int(indice))