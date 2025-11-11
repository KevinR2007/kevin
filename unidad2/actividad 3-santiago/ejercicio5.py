import threading
import time

class LogerDaemon(threading.Thread):
    def __init__(self, intervalo):
        super().__init__(daemon=True)
        self.intervalo = intervalo

    def run(self):
        while True:
            print("[LOG] El programa esta en ejecución...")
            time.sleep(self.intervalo)
            
class TrabajoPesado(threading.Thread):
    def __init__(self, pasos):
        super().__init__()
        self.pasos = pasos
        
    def run(self):
        for i in range(1, self.pasos + 1):
            print(f"Realizando paso {i} de {self.pasos}")
            time.sleep(1)
        print("Trabajo pesado completado.")
        
def main():
    logger = LogerDaemon(intervalo=2)
    trabajador = TrabajoPesado(pasos=5)
    
    logger.start()
    trabajador.start()
    
    trabajador.join()
    
if __name__ == "__main__":
    main()
    