import threading
import queue
import time

class GeneradorTareas(threading.Thread):
    def __init__(self, q, n, consumidores):
        super().__init__()
        self.q = q
        self.n = n
        self.consumidores = consumidores

    def run(self):
        for i in range(1, self.n + 1):
            print(f"Generando tarea: {i}")
            self.q.put(i)
            time.sleep(0.2)

        for _ in range(self.consumidores):
            self.q.put(None)
        print("Generador terminó de enviar tareas.")


class Trabajador(threading.Thread):
    def __init__(self, q, nombre):
        super().__init__()
        self.q = q
        self.nombre = nombre

    def run(self):
        while True:
            tarea = self.q.get()

            if tarea is None:
                print(f"{self.nombre} recibió centinela. Finalizando.")
                self.q.task_done()
                break

            print(f"{self.nombre} procesando {tarea} → resultado: {tarea ** 2}")
            time.sleep(0.5)
            self.q.task_done()


def main():
    q = queue.Queue()
    num_consumidores = 3
    n = 10

    generador = GeneradorTareas(q, n, num_consumidores)
    trabajadores = [Trabajador(q, f"Trabajador-{i+1}") for i in range(num_consumidores)]

    generador.start()
    for t in trabajadores:
        t.start()

    q.join() 
    print("Todas las tareas han sido procesadas.")


if __name__ == "__main__":
    main()
