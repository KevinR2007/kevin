import requests

API_URL = "http://127.0.0.1:8000/api"


# ======================================================
# FUNCIÓN CENTRALIZADA DE PETICIONES HTTP
# ======================================================
def _request(method, url, data=None):
    """
    Ejecuta una petición HTTP al backend.

    Parámetros:
        method (str): Método HTTP (get, post, put, delete).
        url (str): URL completa del endpoint.
        data (dict | None): Datos JSON a enviar cuando aplica.

    Retorna:
        dict: Respuesta JSON del backend o diccionario con error.
    """
    try:
        if method == "get":
            resp = requests.get(url)
        elif method == "post":
            resp = requests.post(url, json=data)
        elif method == "put":
            resp = requests.put(url, json=data)
        elif method == "delete":
            resp = requests.delete(url)
        else:
            return {"error": "Método HTTP no soportado"}

        resp.raise_for_status()

        # Intenta retornar JSON si existe
        try:
            return resp.json()
        except:
            return {"ok": True}  # Para DELETE 204

    except requests.exceptions.Timeout:
        return {"error": "El servidor tardó demasiado en responder."}

    except requests.exceptions.ConnectionError:
        return {"error": "No se pudo conectar con el servidor."}

    except requests.exceptions.HTTPError as http_err:
        return {"error": f"Error HTTP {resp.status_code}", "detalle": str(http_err)}

    except Exception as e:
        return {"error": str(e)}


# ======================================================
# HERRAMIENTAS
# ======================================================
def obtener_herramientas():
    """Obtiene todas las herramientas registradas."""
    return _request("get", f"{API_URL}/herramientas/")


def crear_herramienta(data):
    """Crea una herramienta nueva."""
    return _request("post", f"{API_URL}/herramientas/", data)


def actualizar_herramienta(codigo, data):
    """Actualiza una herramienta usando su código."""
    return _request("put", f"{API_URL}/herramientas/{codigo}/", data)


def eliminar_herramienta(codigo):
    """Elimina una herramienta usando su código."""
    return _request("delete", f"{API_URL}/herramientas/{codigo}/")


# ======================================================
# PRÉSTAMOS
# ======================================================
def obtener_prestamos():
    """Obtiene todos los préstamos registrados."""
    return _request("get", f"{API_URL}/prestamos/")


def crear_prestamo(data):
    """Crea un préstamo nuevo."""
    return _request("post", f"{API_URL}/prestamos/", data)


def actualizar_prestamo(numero_prestamo, data):
    """
    Actualiza un préstamo usando su numero.
    El backend usa /prestamos/<numero>/
    """
    return _request("put", f"{API_URL}/prestamos/{numero_prestamo}/", data)


def eliminar_prestamo(id_prestamo):
    """
    Elimina un préstamo usando su ID real.
    El backend NO usa 'numero' como identificador.
    """
    return _request("delete", f"{API_URL}/prestamos/{id_prestamo}/")




# ======================================================
# BÚSQUEDA
# ======================================================
def buscar(query):
    """Realiza una búsqueda general en el backend."""
    return _request("get", f"{API_URL}/buscar/?q={query}")
