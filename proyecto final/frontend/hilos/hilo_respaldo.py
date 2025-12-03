import threading
import time
from hilos.respaldo_util import registrar_error

class HiloRespaldo(threading.Thread):
    """
    Hilo que ejecuta respaldos automáticos en segundo plano.
    Corre en modo daemon para no bloquear la interfaz.
    """

    def __init__(self, obtener_intervalo, obtener_datos, guardar_respaldo):
        """
        obtener_intervalo: función que devuelve los segundos del intervalo
        obtener_datos: función que retorna el contenido armado
        guardar_respaldo: función que guarda el contenido en disco
        """
        super().__init__(daemon=True)
        self.obtener_intervalo = obtener_intervalo
        self.obtener_datos = obtener_datos
        self.guardar_respaldo = guardar_respaldo

    def run(self):
        """
        Método principal del hilo.
        Se ejecuta en un ciclo infinito: consulta API, arma datos,
        guarda respaldo y espera el intervalo configurado.
        """
        while True:
            try:
                # 1. Leer el intervalo de respaldo
                intervalo = self.obtener_intervalo()

                # 2. Obtener datos desde API (herramientas + préstamos)
                contenido = self.obtener_datos()

                # 3. Guardar el respaldo en disco
                self.guardar_respaldo(contenido)

                # 4. Esperar el intervalo configurado
                time.sleep(intervalo)

            except Exception as e:
                registrar_error(f"Error en HiloRespaldo: {e}")
                time.sleep(5)
