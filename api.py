from fastapi import FastAPI
import requests, json
from tp_redes import buscar_libros_por_lenguaje, buscar_libros_por_author, buscar_libros_entre_anios, buscar_libros_menores_anio, buscar_libros_menores_page,buscar_libros_country, buscar_libros_por_title, buscar_libros_posterior_anio, buscar_libros_pages,buscar_libros_igual_anio, buscar_libros_mayores_page, buscar_libros_entre_pages
url= 'https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json'
libros = requests.get(url).content
libros_json = json.loads(libros)

app = FastAPI()
@app.get("/my-first-api")
def hello():
    return {"Hello world!"}

@app.get("/libros")
def consulta(author=None, title=None,  country=None, lenguage=None, anio=None,anio_desde = None, anio_hasta=None, condicion = None, page=None, page_desde=None,page_hasta=None):
    if author != None:
        lista = buscar_libros_por_author(libros_json, author)
    if title != None:
        lista = buscar_libros_por_title(libros_json, title)
    if country != None:
        lista = buscar_libros_country(libros_json, country)
    if lenguage != None:
        lista = buscar_libros_por_lenguaje(libros_json, lenguage)
    if anio != None:
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