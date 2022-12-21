import yaml


__config = None # generamos una variable global lo inicializamos none nos servira para cachear nuestra config pq estamos leyendo a disco 


def config(): # generamos una funcion
    global __config
    if not __config: #chequeamos si ahi configuracion
        with open('config.yaml', mode='r') as f: #abrimos la configuracion
            __config = yaml.safe_load(f) 

    return __config
