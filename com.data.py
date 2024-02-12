import os
import platform
import socket
import psutil

def get_system_info():
    info = {}
    info['OS'] = platform.system()
    info['OS Version'] = platform.release()
    info['Processor'] = platform.processor()
    info['Hostname'] = socket.gethostname()
    return info

def get_memory_info():
    mem = psutil.virtual_memory()
    info = {}
    info['Total Memory'] = f"{mem.total / (1024 ** 3):.2f} GB"
    info['Available Memory'] = f"{mem.available / (1024 ** 3):.2f} GB"
    info['Used Memory'] = f"{mem.used / (1024 ** 3):.2f} GB"
    return info

def get_network_info():
    info = {}
    info['IP Address'] = socket.gethostbyname(socket.gethostname())
    info['MAC Address'] = ':'.join(['{:02x}'.format((os.getpid() >> i) & 0xff) for i in range(0, 8*6, 8)][::-1])
    return info

def get_cpu_info():
    info = {}
    info['CPU Core Count'] = psutil.cpu_count()
    info['CPU Usage'] = f"{psutil.cpu_percent(interval=0.1)} %"
    return info

def show_info(info):
    for key, value in info.items():
        print(f"{key}: {value}")

def main():
    system_info = get_system_info()
    memory_info = get_memory_info()
    network_info = get_network_info()
    cpu_info = get_cpu_info()

    print("System Info:")
    show_info(system_info)
    print("\nMemory Info:")
    show_info(memory_info)
    print("\nNetwork Info:")
    show_info(network_info)
    print("\nCPU Info:")
    show_info(cpu_info)

if __name__ == "__main__":
    main()
