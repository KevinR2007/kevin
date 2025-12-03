import os
import json

# Ruta del archivo de configuración
RUTA_CONFIG = os.path.join(os.path.dirname(__file__), "intervalo_respaldo.json")

def asegurar_archivo_config():
    """
    Verifica que el archivo de configuración exista.
    Si no existe, lo crea con un valor por defecto.
    """
    if not os.path.exists(RUTA_CONFIG):
        config_inicial = {"intervalo_segundos": 60} #acá se puede cambiar los segundos
        with open(RUTA_CONFIG, "w", encoding="utf-8") as archivo:
            json.dump(config_inicial, archivo, indent=4)

def leer_intervalo_respaldo():
    """
    Lee el intervalo de respaldo desde el archivo JSON de configuración.
    Si algo falla, retorna 60 como valor por defecto.
    """
    try:
        with open(RUTA_CONFIG, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)

        intervalo = data.get("intervalo_segundos", 60)

        # Validar que sea número y mayor a cero
        if not isinstance(intervalo, int) or intervalo <= 0:
            return 60

        return intervalo

    except Exception:
        # Si el archivo está corrupto, no existe o tiene errores
        return 60
