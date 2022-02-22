from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs): #no importa la cantidad de parametros posicionales o nombrados, va a ejecutar la funcion
        initial_time = datetime.now() #nos devuelve la fecha y hora exacta desde el que se ejecuta el codigo
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass


random_func()