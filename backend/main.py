from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"mensagem": "API de monitoramento rodando"}

@app.get("/metricas")
def get_metricas():
    cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory()
    disco = psutil.disk_usage('/')

    return {
        "cpu_percent": cpu,
        "memoria_percent": memoria.percent,
        "memoria_usada_mb": memoria.used // (1024**2),
        "memoria_total_mb": memoria.total // (1024**2),
        "disco_percent": disco.percent,
        "disco_usado_gb": disco.used // (1024**3),
        "disco_total_gb": disco.total // (1024**3)
    }