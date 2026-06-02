// js/charts/ebitdaChart.js

document.addEventListener('DOMContentLoaded', async () => {
    // Buscar dados do mock
    const data = await window.ApiService.getEbitdaData();

    // Renderizar KPIs
    const kpiContainer = document.getElementById('kpi-container');
    const { receitaBruta, receitaLiquida, ebitda, margemEbitda } = data.kpis;
    
    kpiContainer.innerHTML = `
        <div class="kpi-card">
            <div class="kpi-title">Receita Bruta</div>
            <div class="kpi-value">${receitaBruta.value}</div>
            <div class="kpi-trend ${receitaBruta.isPositive ? 'positive' : 'negative'}">${receitaBruta.trend} vs mês anterior</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Receita Líquida</div>
            <div class="kpi-value">${receitaLiquida.value}</div>
            <div class="kpi-trend ${receitaLiquida.isPositive ? 'positive' : 'negative'}">${receitaLiquida.trend} vs mês anterior</div>
        </div>
        <div class="kpi-card highlight-card">
            <div class="kpi-title">EBITDA Realizado</div>
            <div class="kpi-value">${ebitda.value}</div>
            <div class="kpi-trend ${ebitda.isPositive ? 'positive' : 'negative'}">${ebitda.trend} vs mês anterior</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Margem EBITDA</div>
            <div class="kpi-value">${margemEbitda.value}</div>
            <div class="kpi-trend ${margemEbitda.isPositive ? 'positive' : 'negative'}">${margemEbitda.trend} vs mês anterior</div>
        </div>
    `;

    // Gráfico de Evolução Mensal
    const ctxEbitda = document.getElementById('ebitdaChart').getContext('2d');
    new Chart(ctxEbitda, {
        type: 'bar',
        data: {
            labels: data.chartEvolucao.labels,
            datasets: [
                {
                    type: 'line',
                    label: 'Margem EBITDA (%)',
                    data: data.chartEvolucao.margem,
                    borderColor: '#0AE18C',
                    backgroundColor: '#0AE18C',
                    borderWidth: 2,
                    tension: 0.4,
                    yAxisID: 'y1'
                },
                {
                    type: 'bar',
                    label: 'EBITDA (M)',
                    data: data.chartEvolucao.ebitda,
                    backgroundColor: '#14C8FA',
                    borderRadius: 4,
                    yAxisID: 'y'
                },
                {
                    type: 'bar',
                    label: 'Receita Líq (M)',
                    data: data.chartEvolucao.receita,
                    backgroundColor: '#F2F2F2',
                    borderRadius: 4,
                    yAxisID: 'y'
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { beginAtZero: true, grid: { display: false } },
                y1: { beginAtZero: true, position: 'right', grid: { display: false } },
                x: { grid: { display: false } }
            },
            plugins: { legend: { position: 'bottom' } }
        }
    });

    // Gráfico Waterfall (Cascata simplificada)
    const ctxWaterfall = document.getElementById('waterfallChart').getContext('2d');
    new Chart(ctxWaterfall, {
        type: 'bar',
        data: {
            labels: data.chartCascata.labels,
            datasets: [{
                label: 'Impacto R$',
                data: data.chartCascata.data,
                backgroundColor: (ctx) => {
                    const val = ctx.raw;
                    if (ctx.dataIndex === 0 || ctx.dataIndex === 4) return '#00BF63'; // Totals in green
                    return val < 0 ? '#FF3131' : '#0AE18C';
                },
                borderRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { grid: { display: false } },
                x: { grid: { display: false } }
            },
            plugins: { legend: { display: false } }
        }
    });
});
