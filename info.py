import os
import platform
import socket
import psutil
import time
import json
import csv

def collect_data(output_format):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            output_file = 'system_data'
            if output_format == 'json':
                output_file += '.json'
                with open(output_file, 'a') as file:
                    json.dump(data, file)
            elif output_format == 'csv':
                output_file += '.csv'
                with open(output_file, 'a') as file:
                    writer = csv.DictWriter(file, fieldnames=data.keys())
                    if file.tell() == 0:
                        writer.writeheader()
                    writer.writerow(data)
            else:
                raise ValueError('Неподдерживаемый формат вывода.')
            return data
        return wrapper
    return decorator

@collect_data('json')
def get_system_info():
    info = {}
    info['Операционная система'] = platform.system()
    info['Версия операционной системы'] = platform.release()
    info['Процессор'] = platform.processor()
    info['Имя хоста'] = socket.gethostname()
    return info

@collect_data('json')
def get_memory_info():
    mem = psutil.virtual_memory()
    info = {}
    info['Всего памяти'] = f"{mem.total / (1024 ** 3):.2f} ГБ"
    info['Доступно памяти'] = f"{mem.available / (1024 ** 3):.2f} ГБ"
    info['Используется памяти'] = f"{mem.used / (1024 ** 3):.2f} ГБ"
    info['Запас памяти'] = f"{mem.percent} %"
    return info

@collect_data('json')
def get_network_info():
    info = {}
    info['IP адрес'] = socket.gethostbyname(socket.gethostname())
    info['Имя хоста'] = socket.gethostname()
    return info

@collect_data('json')
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

        time.sleep(1)

if __name__ == '__main__':
    main()