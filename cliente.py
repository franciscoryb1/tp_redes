#from fastapi import FastAPI
import requests, json
#from tp_redes import buscar_libros_por_lenguaje, borrar_libro, buscar_libros_por_author, buscar_libros_entre_anios, buscar_libros_menores_anio, buscar_libros_menores_page,buscar_libros_country, buscar_libros_por_title, buscar_libros_posterior_anio, buscar_libros_pages,buscar_libros_igual_anio, buscar_libros_mayores_page, buscar_libros_entre_pages

print("""que queres hacer?
      1- Consultar los libros
      2- Borrar libros
      3- Insertar libros""")

x = input('Ingrese una opcion: ')

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
    if b == '1':
        libro = input('Ingrese el titulo del libro: ')
        resp = requests.get("http://127.0.0.1:8000/libros", params={"title":libro})
        data_dict = resp.json()
        print(data_dict)
    if b == '2':
        libro = input('Ingrese el author del libro: ')
        resp = requests.get("http://127.0.0.1:8000/libros", params={"author":libro})
        print(resp.content)
    if b == '3':
        libro = input('Ingrese el country del libro: ')
        resp = requests.get("http://127.0.0.1:8000/libros", params={"country":libro})
        print(resp.content)
    if b == '4':
        libro = input('Ingrese el year del libro: ')
        condicion = input("""Ingrese una condicion:
                          e) Solo del año especificado
                          a) Anteriores al año especificado
                          p) Posteriores al año especificado: """)
        resp = requests.get("http://127.0.0.1:8000/libros", params={"anio":libro, "condicion":condicion})
        print(resp.content)
    if b == '5':
        libro = input('Ingrese el page del libro: ')
        resp = requests.get("http://127.0.0.1:8000/libros", params={"page":libro})
        print(resp.content)
    if b == '6':
        libro = input('Ingrese el language del libro: ')
        resp = requests.get("http://127.0.0.1:8000/libros", params={"language":libro})
        print(resp.content)
    if b == '7':
        anio_1 = input('Ingrese el primer año: ')
        anio_2 = input('Ingrese el segundo año: ')
        resp = requests.get("http://127.0.0.1:8000/libros", params={"anio_desde":anio_1, "anio_hasta":anio_2})
        print(resp.content)


if x == '2':
    libro = input('Ingrese el titulo del libro que quiere eliminar: ')
    resp = requests.get("http://127.0.0.1:8000/libros", params={"title":libro})
    libros_a_eliminar = list(resp.json().values())
    indices_a_eliminar = list(resp.json().keys())
    print(f'estos son los libros que se eliminarán: {libros_a_eliminar}')
    confirmacion = input('Está seguro de que desea eliminarlos?: ')
    if confirmacion.lower() == 'si':
        resp_2 = requests.delete("http://127.0.0.1:8000/delete", params={"lista":indices_a_eliminar})
        print(resp_2.status_code)
    if confirmacion.lower() == 'no':
        print('Los libros no han sido eliminados')


if x == '3':
    print('insertar')

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


