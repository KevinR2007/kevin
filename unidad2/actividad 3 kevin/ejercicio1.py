import threading
import time

def tarea(nombre, duracion):
    print(f"inicio de la tarea {nombre} (duracion={duracion}s)")  #la s es de segundos
    time.sleep(duracion)
    print(f"fin de la tarea {nombre}")
    
    
def main():
    hilo1 = threading.Thread(target=tarea, args=("A", 1))
    hilo2 = threading.Thread(target=tarea, args=("B", 2))
    hilo3 = threading.Thread(target=tarea, args=("C", 3))
    
    hilo1.start()
    hilo2.start()
    hilo3.start()
    
    hilo1.join()
    hilo2.join()
    hilo3.join()
    
    
    print("tareas terminadas")
    
if __name__ == "__main__":
    main()