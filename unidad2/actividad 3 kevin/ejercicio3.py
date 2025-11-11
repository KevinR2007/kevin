import threading
import random
import time


class Cuenta:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.lock = threading.Lock()
        
        
    def depositar(self, monto):
        with self.lock:
            saldo_actual = self.saldo
            saldo_actual += monto
            time.sleep(0.01)  
            self.saldo = saldo_actual
            print(f"Depositado {monto},  saldo actual: {self.saldo}")
            
    def retirar(self, monto):
        with self.lock:
            if self.saldo >= monto:
                saldo_actual = self.saldo
                saldo_actual -= monto
                time.sleep(0.01)  
                self.saldo = saldo_actual
                print(f"Retirado {monto},  saldo actual: {self.saldo}")
            else:
                print(f"Fondos insuficientes para retirar {monto}, saldo : {self.saldo}")
                
                
class OperadorCuenta(threading.Thread):
    def __init__(self, cuenta, operaciones):
        super().__init__()
        self.cuenta = cuenta
        self.operaciones = operaciones

    def run(self):
        for _ in range(self.operaciones):
            monto = random.randint(1, 100)
            if random.choice([True, False]):
                self.cuenta.depositar(monto)
            else:
                self.cuenta.retirar(monto)
            time.sleep(0.01)

                
                
def main():
    cuenta = Cuenta(saldo_inicial=1000)
    hilos = [OperadorCuenta(cuenta, 5) for _ in range(4)]
        
    for hilo in hilos:
            hilo.start()
            
            
            
    for hilo in hilos:
            hilo.join()
            
            
    print(f"Saldo final: {cuenta.saldo}")
        
        
if __name__ == "__main__":
    main()
        