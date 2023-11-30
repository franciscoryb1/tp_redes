#from fastapi import FastAPI
import requests, json
#from tp_redes import buscar_libros_por_lenguaje, borrar_libro, buscar_libros_por_author, buscar_libros_entre_anios, buscar_libros_menores_anio, buscar_libros_menores_page,buscar_libros_country, buscar_libros_por_title, buscar_libros_posterior_anio, buscar_libros_pages,buscar_libros_igual_anio, buscar_libros_mayores_page, buscar_libros_entre_pages

ip = "http://192.168.0.9"
puerto = ":8080"
url = ip + puerto

print("""que queres hacer?
      1- Consultar los libros
      2- Borrar libros
      3- Insertar libros""")

x = input('Ingrese una opcion: ')

# Consultar los libros 
if x == '1':
    print('buscar')
    print("""Buscar por:
          1) Title
          2) Author
          3) Country
          4) year
          5) Page
          6) Language
          7) anio_entre""")
    b = input('Ingrese una opcion: ')
    # Buscar por titulo FUNCIONA
    if b == '1':
        libro = input('Ingrese el titulo del libro: ')
        resp = requests.get(url + '/libros', params={"title":libro})
        data_dict = resp.json()
        for i in data_dict:
            print(i)
    # Buscar por autor FUNCIIONA
    if b == '2':
        libro = input('Ingrese el author del libro: ')
        resp = requests.get(url + '/libros', params={"author":libro})
        data_dict = resp.json()
        for i in data_dict:
            print(i)
    # Buscar por país FUNCIONA
    if b == '3':
        libro = input('Ingrese el country del libro: ')
        resp = requests.get(url + '/libros', params={"country":libro})
        data_dict = resp.json()
        for i in data_dict:
            print(i)
    # Buscar por anio NO
    if b == '4':
        libro = input('Ingrese el year del libro: ')
        condicion = input("""Ingrese una condicion:
                          e) Solo del año especificado
                          a) Anteriores al año especificado
                          p) Posteriores al año especificado: """)
        resp = requests.get(url + '/libros', params={"anio":libro, "condicion":condicion})
        print(resp.content)
    # Buscar por paginas NO
    if b == '5':
        libro = input('Ingrese el page del libro: ')
        resp = requests.get(url + '/libros', params={"page":libro})
        print(resp.content)
    # Buscar por lenguaje FUNCIONA
    if b == '6':
        libro = input('Ingrese el language del libro: ')
        resp = requests.get(url + '/libros', params={"language":libro})
        data_dict = resp.json()
        for i in data_dict:
            print(i)
    # Buscar entre años FUNCIONA
    if b == '7':
        anio_1 = input('Ingrese el primer año: ')
        anio_2 = input('Ingrese el segundo año: ')
        resp = requests.get(url + '/libros', params={"anio_desde":anio_1, "anio_hasta":anio_2})
        data_dict = resp.json()
        for i in data_dict:
            print(i)

# BORRAR un libro por titulo FUNCIONA
if x == '2':
    libro = input("Ingrese el titulo del libro que desea eliminar: ")
    print("Se eliminaran los siguientes libros:")
    resp_1 = requests.get(url + '/libros', params={"title":libro})
    data_dict = resp_1.json()
    for i in data_dict:
        print(i)
    #print(data_dict)
    conf = input("Esta seguro de que desea eliminarlos? ")
    if conf == "si":
        resp_2 = requests.delete(url + '/delete', params={"title":libro})
        print("Se eliminaron los siguientes libros")
        data_dict_2 = resp_2.json()
        print(data_dict_2)
        print(resp_2.status_code)
    if conf == "no":
        print("No se eliminaron los libros.")


if x == '3':
    print('insertar')
    print("""Para insertar un libro debera completar los siguientes datos:
          1) Autor
          2) Pais
          3) imageLink
          4) Lenguaje
          5) Link
          6) Numero de paginas
          7) Titulo
          8) Año""")
    autor = input("1) Autor: ")
    pais = input("2) Pais: ")
    imageLink = input("3) imageLink: ")
    lenguaje = input("4) Lenguaje: ")
    link = input("5) Link: ")
    paginas = input("6) Paginas: ")
    titulo = input("7) Titulo: ")
    anio = input("8) Año: ")
    resp = requests.put(url + '/put', params={"author":autor, "title": titulo, "year": anio, "page": paginas, "language": lenguaje, "country": pais, "imageLink": imageLink, "link": link})
    data_dict = resp.json()
    for i in data_dict:
        print(i)
# INSERTAR un nuevo libro
# if x == '3':
#     print('insertar')
#     print("""Para insertar un libro debera completar los siguientes datos:
#           1) Autor
#           2) Pais
#           3) imageLink
#           4) Lenguaje
#           5) Link
#           6) Numero de paginas
#           7) Titulo
#           8) Año""")
#     autor = input("1) Autor: ")
#     pais = input("2) Pais: ")
#     imageLink = input("3) imageLink: ")
#     lenguaje = input("4) Lenguaje: ")
#     link = input("5) Link: ")
#     paginas = input("6) Paginas: ")
#     titulo = input("7) Titulo: ")
#     anio = input("8) Año: ")
    
#     nuevo_libro = {
#         "author": str(autor),
#         "country": str(pais),
#         "imageLink": str(imageLink),
#         "language": str(lenguaje),
#         "link": str(link),
#         "pages": int(paginas),
#         "title": str(titulo),
#         "year": int(anio)}
#     nuevo = {
#     "author": "Unknown",
#     "country": "Achaemenid Empire",
#     "imageLink": "images/the-book-of-job.jpg",
#     "language": "Hebrew",
#     "link": "https://en.wikipedia.org/wiki/Book_of_Job\n",
#     "pages": 176,
#     "title": "The Book Of Job",
#     "year": -600
#   }
#     resp = requests.put("http://127.0.0.1:8000/put", params={"libro":nuevo_libro})
#     print(resp.status_code)

# Función para insertar un nuevo libro con datos proporcionados por el usuario
# def insertar_libro_manual(libros):
#     nuevo_libro = {
#         "author": input("Autor: "),
#         "country": input("País: "),
#         "imageLink": input("Enlace de la imagen: "),
#         "language": input("Idioma: "),
#         "link": input("Enlace: "),
#         "pages": int(input("Número de páginas: ")),
#         "title": input("Título: "),
#         "year": int(input("Año: "))
#     }
#     libros.append(nuevo_libro)
#     print("Libro insertado correctamente.")


# # Llamar a la función para insertar un nuevo libro con datos proporcionados por el usuario
# insertar_libro_manual(libros_json)

# # Guardar el JSON actualizado
# guardar_json(ruta_del_json, libros_json)

# # Imprimir la lista actualizada (opcional)
# print(libros_json)
