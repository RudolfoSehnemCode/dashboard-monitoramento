const maxPontos = 20;
const labels = [];
const dadosCpu = [];
const dadosMemoria = [];

const ctx = document.getElementById('grafico').getContext('2d');
const grafico = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [
            {
                label: 'CPU %',
                data: dadosCpu,
                borderColor: '#00ff9c',
                backgroundColor: 'rgba(0, 255, 156, 0.1)',
                tension: 0.3,
                fill: true
            },
            {
                label: 'Memória %',
                data: dadosMemoria,
                borderColor: '#00b8ff',
                backgroundColor: 'rgba(0, 184, 255, 0.1)',
                tension: 0.3,
                fill: true
            }
        ]
    },
    options: {
        responsive: true,
        scales: {
            y: { min: 0, max: 100, grid: { color: '#2a2a3d' }, ticks: { color: '#8888aa' } },
            x: { grid: { color: '#2a2a3d' }, ticks: { color: '#8888aa' } }
        },
        plugins: {
            legend: { labels: { color: '#e0e0e0' } }
        }
    }
});

async function atualizarMetricas() {
    try {
        const resposta = await fetch("http://127.0.0.1:8000/metricas");
        const dados = await resposta.json();

        document.getElementById("cpu").innerText = dados.cpu_percent + "%";
        document.getElementById("memoria").innerText = dados.memoria_percent + "%";
        document.getElementById("disco").innerText = dados.disco_percent + "%";

        document.getElementById("barra-cpu").style.width = dados.cpu_percent + "%";
        document.getElementById("barra-memoria").style.width = dados.memoria_percent + "%";
        document.getElementById("barra-disco").style.width = dados.disco_percent + "%";

        const agora = new Date().toLocaleTimeString();
        labels.push(agora);
        dadosCpu.push(dados.cpu_percent);
        dadosMemoria.push(dados.memoria_percent);

        if (labels.length > maxPontos) {
            labels.shift();
            dadosCpu.shift();
            dadosMemoria.shift();
        }

        grafico.update();
    } catch (erro) {
        console.error("Erro ao buscar métricas:", erro);
    }
}

atualizarMetricas();
setInterval(atualizarMetricas, 3000);