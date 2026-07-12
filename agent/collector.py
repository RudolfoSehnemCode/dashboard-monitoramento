import psutil
import time

def coletar_metricas():
    cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory()
    disco = psutil.disk_usage('/')

    print(f"CPU: {cpu}%")
    print(f"RAM: {memoria.percent}% usada ({memoria.used // (1024**2)} MB de {memoria.total // (1024**2)} MB)")
    print(f"Disco: {disco.percent}% usado ({disco.used // (1024**3)} GB de {disco.total // (1024**3)} GB)")
    print("-" * 40)

if __name__ == "__main__":
    while True:
        coletar_metricas()
        time.sleep(2)

