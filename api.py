from fastapi import FastAPI
import requests, json
from tp_redes import buscar_libros_por_lenguaje, borrar, borrar_por_titulo, buscar_libros_por_author, buscar_libros_entre_anios, buscar_libros_menores_anio, buscar_libros_menores_page,buscar_libros_country, buscar_libros_por_title, buscar_libros_posterior_anio, buscar_libros_pages,buscar_libros_igual_anio, buscar_libros_mayores_page, buscar_libros_entre_pages
url= 'https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json'
libros = requests.get(url).content
libros_json = json.loads(libros)


# # Cargar el JSON desde el archivo
# ruta_del_json = "file.json"  # Reemplaza con la ruta correcta
# with open(ruta_del_json, 'r') as file:
#     libros_json = json.load(file)

app = FastAPI()
@app.get("/my-first-api")
def hello():
    return {"Hello world!"}

@app.get("/libros")
def consulta(ho = None, author=None, title=None,  country=None, lenguage=None, anio=None,anio_desde = None, anio_hasta=None, condicion = None, page=None, page_desde=None,page_hasta=None):
    if ho != None:
        lista = len(libros_json)
        #lista = libros_json
    if author != None:
        print(len(libros_json))
        lista = buscar_libros_por_author(libros_json, author)
    if title != None:
        lista = buscar_libros_por_title(libros_json, title)
        # lista = list(buscar_libros_por_title(libros_json, title).values())
    if country != None:
        lista = buscar_libros_country(libros_json, country)
    if lenguage != None:
        lista = buscar_libros_por_lenguaje(libros_json, lenguage)
    if anio != None:
        lista = []
        if condicion == None:
            return 'Error: Debe ingresar una condicion.'
        if condicion == 'a':
            lista = buscar_libros_menores_anio(libros_json, int(anio))
        if condicion == 'p':
            lista = buscar_libros_posterior_anio(libros_json, int(anio))
        if condicion == 'e':
            lista = buscar_libros_igual_anio(libros_json, int(anio))
    if anio_desde != None and anio_hasta != None:
        lista = buscar_libros_entre_anios(libros_json, anio_desde, anio_hasta)
    if page != None:
        lista = []
        if condicion == None:
            return 'Error: Debe ingresar una condicion.'
        if condicion == 'a':
            lista = buscar_libros_menores_page(libros_json, page)
        if condicion == 'p':
            lista = buscar_libros_mayores_page(libros_json, page)
        if condicion == 'e':
            lista = buscar_libros_pages(libros_json, page)
    if page_desde != None and page_hasta != None:
        lista = buscar_libros_entre_pages(libros_json, int(page_desde), int(page_hasta))

    return lista

@app.delete("/delete")
def query(title):
    return borrar_por_titulo(libros_json, title)


@app.put("/put")
def insertar_libro(libro):
    return libros_json.append(libro)

# Función para insertar un nuevo libro con datos proporcionados por el usuario
def insertar_libro_manual(author=None, title=None, year=None, page=None, language=None, country=None, imageLink=None, link=None):
    nuevo_libro = {
        "author": author,
        "title": title,
        "year": year,
        "pages": page,
        "language": language,
        "country": country,
        "imageLink": imageLink,
        "link": link
    }
    libros_json.append(nuevo_libro)
    return nuevo_libro


# # Llamar a la función para insertar un nuevo libro con datos proporcionados por el usuario
# insertar_libro_manual(libros_json)

# # Guardar el JSON actualizado
# guardar_json(ruta_del_json, libros_json)

# # Imprimir la lista actualizada (opcional)
# print(libros_json)
