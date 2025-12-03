from django.apps import AppConfig


class ApiConfig(AppConfig):
    """ Configuración de la aplicación 'api' del proyecto Django.
    
    Esta clase le indica a django como debe iniciar la aplicación.
    
        Atributos:
        default_auto_field (str): Tipo de campo predeterminado para los modelos.
        name (str): Nombre de la aplicación. debe coincidir con el nombre del directorio.
        
        
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
