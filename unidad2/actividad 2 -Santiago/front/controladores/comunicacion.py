import requests

class Comunicacion:

    def __init__(self, ventanaPrincipal):
        self.url = 'http://localhost:8000/v1/clase'
        self.ventanaPrincipal = ventanaPrincipal

    def guardar(self, tema, descripcion, numero_clase):
        try:
            print(tema, descripcion, numero_clase)
            data = {
                'tema': tema,
                'descripcion': descripcion,
                'numero_clase': int(numero_clase)
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json())  # 👈 se corrige el paréntesis
            return resultado
        except Exception as e:
            print(f"Error al guardar: {e}")
            return None

    def consultar(self, id):
        try:
            resultado = requests.get(f"{self.url}/{id}")
            return resultado.json()
        except Exception as e:
            print(f"Error al consultar id {id}: {e}")
            return None

    def consultarTodo(self, titulo=None, descripcion=None, numero=None):
        try:
            url = self.url
            if numero is not None:
                url += f"?numero_clase={numero}"  # 👈 construye correctamente el query param
            print(url)
            resultado = requests.get(url)
            return resultado.json()
        except Exception as e:
            print(f"Error al consultar todo: {e}")
            return None
