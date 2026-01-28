# Biblioteca API · 100 libros clásicos

API REST académica para consultar, filtrar y administrar un catálogo de libros clásicos, desarrollada con **FastAPI**. La aplicación consume el dataset público **“100 Best Books”** y expone endpoints para realizar búsquedas avanzadas por autor, título, país, idioma, rangos de año y cantidad de páginas.

El proyecto está orientado a prácticas de redes y servicios web, priorizando claridad en el diseño de endpoints, correcta gestión de parámetros y consumo de datos remotos en formato JSON.

---

## Objetivo

Ofrecer una base sólida para el aprendizaje y la experimentación en el desarrollo de servicios web, con foco en:

* Consumo de datos remotos en formato JSON.
* Diseño e implementación de endpoints RESTful.
* Consultas flexibles mediante parámetros de URL.
* Operaciones básicas de CRUD (lectura, inserción y eliminación).

---

## Tecnologías

* **Python 3**
* **FastAPI**
* **Requests**

---

## Fuente de datos

El catálogo se obtiene desde el siguiente dataset público:

* [https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json](https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json)

---

## Estructura del proyecto

* `api.py`: servidor FastAPI con los endpoints de consulta, inserción y eliminación.
* `tp_redes.py`: funciones de búsqueda y utilidades sobre el dataset.
* `cliente.py`: cliente interactivo de consola para consumir la API.

---

## Ejecución

1. Crear y activar un entorno virtual (opcional):

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

---

## Instalación

Instalar dependencias:

```bash
pip install fastapi uvicorn requests
```

---

## Ejecución

2. Iniciar la API:

```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

---

## Ejecución

1. Crear y activar un entorno virtual (opcional):

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
```

2. Iniciar la API:

```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

---

## Endpoints disponibles

### GET /my-first-api

Endpoint de prueba para verificar el funcionamiento del servidor.

Respuesta:

```json
{"Hello world!"}
```

---

### GET /libros

Permite filtrar el catálogo por múltiples criterios, combinando distintos parámetros según la necesidad.

**Parámetros disponibles:**

* `author`: autor/a del libro.
* `title`: título del libro.
* `country`: país de origen.
* `lenguage`: idioma (tal como figura en el dataset).
* `anio`: año específico con condición.
* `condicion`:

  * `a`: anteriores al año indicado.
  * `p`: posteriores al año indicado.
  * `e`: exactamente el año indicado.
* `anio_desde` y `anio_hasta`: rango de años.
* `page`: número de páginas con condición.
* `page_desde` y `page_hasta`: rango de páginas.

**Ejemplos de uso:**

```bash
# Buscar por autor
curl "http://localhost:8000/libros?author=Kafka"

# Buscar por título
curl "http://localhost:8000/libros?title=Odyssey"

# Buscar por año (anteriores a 1900)
curl "http://localhost:8000/libros?anio=1900&condicion=a"

# Buscar por rango de años
curl "http://localhost:8000/libros?anio_desde=1800&anio_hasta=1899"
```

---

### DELETE /delete

Elimina libros del catálogo en memoria a partir de su título.

**Parámetros:**

* `title`: título del libro a eliminar.

**Ejemplo:**

```bash
curl -X DELETE "http://localhost:8000/delete?title=The%20Odyssey"
```

---

### PUT /put

Inserta un nuevo libro en el catálogo en memoria durante la ejecución de la API.

**Parámetros:**

* `author`, `title`, `year`, `page`, `language`, `country`, `imageLink`, `link`

**Ejemplo:**

```bash
curl -X PUT "http://localhost:8000/put?author=Autor&title=Titulo&year=2024&page=120&language=Español&country=Argentina&imageLink=img.jpg&link=https://example.com"
```

---

## Cliente de consola (opcional)

Para consumir la API mediante un menú interactivo desde consola, ejecutar:

```bash
python cliente.py
```

Nota: el cliente utiliza una IP y puerto específicos; se recomienda ajustarlos en `cliente.py` si se ejecuta en un entorno local distinto.

---

## Alcance académico

Este repositorio está orientado a prácticas de redes y servicios web y puede utilizarse como base para:

* Ejercicios de consultas por parámetros.
* Pruebas de clientes HTTP.
* Extensiones con persistencia o integración con bases de datos.

**Autoría académica:** trabajo práctico de redes/comunicaciones, con fines educativos.
