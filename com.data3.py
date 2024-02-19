import os
import platform
import socket
import psutil
import time

def collect_data(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        with open('system_data.txt', 'a') as file:
            file.write(f'{time.ctime()}\n')
            for key, value in data.items():
                file.write(f'{key}: {value}\n')
            file.write('\n')
        return data
    return wrapper

@collect_data
def get_system_info():
    info = {}
    info['Операционная система'] = platform.system()
    info['Версия операционной системы'] = platform.release()
    info['Процессор'] = platform.processor()
    info['Имя хоста'] = socket.gethostname()
    return info

@collect_data
def get_memory_info():
    mem = psutil.virtual_memory()
    info = {}
    info['Всего памяти'] = f"{mem.total / (1024 ** 3):.2f} ГБ"
    info['Доступно памяти'] = f"{mem.available / (1024 ** 3):.2f} ГБ"
    info['Используется памяти'] = f"{mem.used / (1024 ** 3):.2f} ГБ"
    info['Запас памяти'] = f"{mem.percent} %"
    return info

@collect_data
def get_network_info():
    info = {}
    info['IP адрес'] = socket.gethostbyname(socket.gethostname())
    info['Имя хоста'] = socket.gethostname()
    return info

@collect_data
def get_cpu_info():
    info = {}
    info['Модель процессора'] = platform.processor()
    info['Количество ядер'] = psutil.cpu_count()
    info['Частота процессора'] = f"{psutil.cpu_freq().current / 1000:.2f} ГГц"
    return info

def show_info(data):
    for key, value in data.items():
        print(f'{key}: {value}')

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("Информация о системе:")
        system_info = get_system_info()
        show_info(system_info)
        
        print("\nИнформация о памяти:")
        memory_info = get_memory_info()
        show_info(memory_info)
        
        print("\nИнформация о сети:")
        network_info = get_network_info()
        show_info(network_info)
        
        print("\nИнформация о процессоре:")
        cpu_info = get_cpu_info()
        show_info(cpu_info)
        
        print("\n----------------------------------\n")
        
        time.sleep(5) 

if __name__ == '__main__':
    main()