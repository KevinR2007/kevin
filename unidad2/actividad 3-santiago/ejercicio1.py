#primer ejercicio 

import threading
import time

def tarea(nombre, duracion):
    print(f"inicio de la tarea {nombre} (duracion={duracion})")
    time.sleep(duracion)
    print(f"fin de la tarea {nombre}")
    
def main():
    hilo1 = threading.Thread(target=tarea, args=("hilo 1", 1))
    hilo2 = threading.Thread(target=tarea, args=("hilo 2", 3))
    hilo3 = threading.Thread(target=tarea, args=("hilo 3", 2))
    
    hilo1.start()
    hilo2.start()
    hilo3.start()
    
    hilo1.join()
    hilo2.join()
    hilo3.join()
    
    print("terminado")
    
if __name__ == "__main__":
    main()