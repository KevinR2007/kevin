import os
from controladores.comunicacion import API_URL
import requests
import json
from datetime import datetime

# Ruta donde se guardarán los respaldos
RUTA_RESPALDOS = os.path.join(os.path.dirname(__file__), "respaldos")

def asegurar_carpeta_respaldo():
    """
    Verifica que la carpeta de respaldos exista.
    Si no existe, la crea.
    """
    if not os.path.exists(RUTA_RESPALDOS):
        os.makedirs(RUTA_RESPALDOS)


def obtener_herramientas():
    """
    Consulta la API del backend para obtener todas las herramientas.
    Retorna una lista de diccionarios.
    """
    try:
        url = f"{API_URL}/herramientas/"
        respuesta = requests.get(url, timeout=5)

        if respuesta.status_code == 200:
            return respuesta.json()

        return []

    except Exception as e:
        registrar_error(f"Error al obtener herramientas: {e}")
        return []


def obtener_prestamos():
    """
    Consulta la API del backend para obtener todos los préstamos.
    Retorna una lista de diccionarios.
    """
    try:
        url = f"{API_URL}/prestamos/"
        respuesta = requests.get(url, timeout=5)

        if respuesta.status_code == 200:
            return respuesta.json()

        return []

    except Exception as e:
        registrar_error(f"Error al obtener préstamos: {e}")
        return []


def armar_contenido_respaldo(herramientas, prestamos):
    """
    Junta los datos de herramientas y préstamos en un solo diccionario.
    """
    return {
        "herramientas": herramientas if isinstance(herramientas, list) else [],
        "prestamos": prestamos if isinstance(prestamos, list) else []
    }


def guardar_respaldo(contenido):
    """
    Guarda el contenido del respaldo en un archivo JSON dentro
    de la carpeta de respaldos.
    """
    try:
        asegurar_carpeta_respaldo()

        # Crear nombre del archivo
        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f"respaldo_{fecha}.json"
        ruta_completa = os.path.join(RUTA_RESPALDOS, nombre_archivo)

        # Guardar JSON
        with open(ruta_completa, "w", encoding="utf-8") as archivo:
            json.dump(contenido, archivo, ensure_ascii=False, indent=4)

    except Exception as e:
        registrar_error(f"Error al guardar respaldo: {e}")


# Archivo donde se registran errores del sistema de respaldo
RUTA_ERRORES = os.path.join(os.path.dirname(__file__), "errores_respaldo.json")

def registrar_error(mensaje):
    """
    Registra un error en errores_respaldo.json sin detener la app.
    """
    evento = {
        "fecha": datetime.now().isoformat(),
        "error": mensaje
    }

    try:
        # Leer errores previos si existen
        if os.path.exists(RUTA_ERRORES):
            with open(RUTA_ERRORES, "r", encoding="utf-8") as f:
                errores = json.load(f)
        else:
            errores = []

        # Agregar nuevo error
        errores.append(evento)

        # Guardar archivo
        with open(RUTA_ERRORES, "w", encoding="utf-8") as f:
            json.dump(errores, f, indent=4, ensure_ascii=False)

    except Exception:
        pass
