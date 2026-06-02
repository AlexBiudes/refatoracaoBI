// js/charts/custosChart.js

document.addEventListener('DOMContentLoaded', async () => {
    const data = await window.ApiService.getCustosData();

    // Renderizar KPIs
    const kpiContainer = document.getElementById('kpi-container');
    const { custoTotal, custoMedio, percentualReceita } = data.kpis;
    
    kpiContainer.innerHTML = `
        <div class="kpi-card">
            <div class="kpi-title">Custo Total (Mês Atual)</div>
            <div class="kpi-value">${custoTotal.value}</div>
            <div class="kpi-trend ${custoTotal.isPositive ? 'positive' : 'negative'}">${custoTotal.trend} vs mês anterior</div>
        </div>
        <div class="kpi-card highlight-card">
            <div class="kpi-title">Custo Médio por Produto</div>
            <div class="kpi-value">${custoMedio.value}</div>
            <div class="kpi-trend ${custoMedio.isPositive ? 'positive' : 'negative'}">${custoMedio.trend} vs mês anterior</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">% Custos sobre Receita</div>
            <div class="kpi-value">${percentualReceita.value}</div>
            <div class="kpi-trend ${percentualReceita.isPositive ? 'positive' : 'negative'}">${percentualReceita.trend} vs mês anterior</div>
        </div>
    `;

    // Gráfico de Grupos de Custo
    const ctxCostGroup = document.getElementById('costGroupChart').getContext('2d');
    new Chart(ctxCostGroup, {
        type: 'bar',
        data: {
            labels: data.chartGrupos.labels,
            datasets: [
                {
                    label: 'Mês Atual',
                    data: data.chartGrupos.atual,
                    backgroundColor: '#14C8FA',
                    borderRadius: 4
                },
                {
                    label: 'Mês Anterior',
                    data: data.chartGrupos.anterior,
                    backgroundColor: '#F2F2F2',
                    borderRadius: 4
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { grid: { display: false } },
                x: { grid: { display: false } }
            }
        }
    });
});
