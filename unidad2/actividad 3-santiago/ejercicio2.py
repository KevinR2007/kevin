import threading
import time

class Temporizador(threading.Thread):
    def __init__(self, limite, reset_event, stop_event):
        super().__init__()
        self.limite = limite
        self.reset_event = reset_event
        self.stop_event = stop_event

    def run(self):
        i = 0
        while not self.stop_event.is_set():
            print(f"Tiempo: {i} s")
            time.sleep(1)
            i += 1

            if self.reset_event.is_set():
                print("Reinicio del temporizador.\n")
                i = 0
                self.reset_event.clear()

            if i >= self.limite:
                print("¡Tiempo límite alcanzado!")
                self.stop_event.set()
                break


class EscuchaReset(threading.Thread):
    def __init__(self, reset_event):
        super().__init__(daemon=True)
        self.reset_event = reset_event

    def run(self):
        while True:
            input()  
            self.reset_event.set()
            pass


def main():
    reset_event = threading.Event()
    stop_event = threading.Event()

    temporizador = Temporizador(limite=10, reset_event=reset_event, stop_event=stop_event)
    escucha = EscuchaReset(reset_event=reset_event)

    escucha.start()
    temporizador.start()
    temporizador.join()
    pass


if __name__ == "__main__":
    main()