from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "API de monitoramento rodando"}


def test_metricas():
    response = client.get("/metricas")
    assert response.status_code == 200
    data = response.json()

    campos_esperados = [
        "cpu_percent",
        "memoria_percent",
        "memoria_usada_mb",
        "memoria_total_mb",
        "disco_percent",
        "disco_usado_gb",
        "disco_total_gb",
    ]
    for campo in campos_esperados:
        assert campo in data

    assert 0 <= data["cpu_percent"] <= 100
    assert 0 <= data["memoria_percent"] <= 100
    assert 0 <= data["disco_percent"] <= 100
