import threading
import time

#loggerdeamon siempre va a ser un hilo aparte 
class Logger(threading.Thread):
    def __init__(self, intervalo):
        super().__init__(daemon=True)
        self.intervalo = intervalo
        
        
    def run(self):
        while True:
            print("Logger: El programa sigue en ejecución...")
            time.sleep(self.intervalo)
            
class TrabajoPesado(threading.Thread):
    def __init__(self, pasos):
        super().__init__()
        self.pasos = pasos
    
    def run(self):
        for i in range(1, self.pasos + 1):
            print(f"Trabajo pesado: paso {i} de {self.pasos}")
            time.sleep(1)
        print("Trabajo pesado: tarea completada.")
        
def main():
    logger = Logger(intervalo=3)
    trabajo = TrabajoPesado(pasos=5)
    
    logger.start()
    trabajo.start()
    
    trabajo.join()
    
if __name__ == "__main__":
    main()