// js/charts/rentabilidadeChart.js

document.addEventListener('DOMContentLoaded', async () => {
    const data = await window.ApiService.getRentabilidadeData();

    // Renderizar KPIs
    const kpiContainer = document.getElementById('kpi-container');
    const { lucroBruto, margemBruta, lucroLiquido, margemLiquida } = data.kpis;
    
    kpiContainer.innerHTML = `
        <div class="kpi-card">
            <div class="kpi-title">Lucro Bruto</div>
            <div class="kpi-value">${lucroBruto.value}</div>
            <div class="kpi-trend ${lucroBruto.isPositive ? 'positive' : 'negative'}">${lucroBruto.trend} YoY</div>
        </div>
        <div class="kpi-card highlight-card">
            <div class="kpi-title">Margem Bruta</div>
            <div class="kpi-value">${margemBruta.value}</div>
            <div class="kpi-trend ${margemBruta.isPositive ? 'positive' : 'negative'}">${margemBruta.trend} YoY</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Lucro Líquido</div>
            <div class="kpi-value">${lucroLiquido.value}</div>
            <div class="kpi-trend ${lucroLiquido.isPositive ? 'positive' : 'negative'}">${lucroLiquido.trend} YoY</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Margem Líquida</div>
            <div class="kpi-value">${margemLiquida.value}</div>
            <div class="kpi-trend ${margemLiquida.isPositive ? 'positive' : 'negative'}">${margemLiquida.trend} YoY</div>
        </div>
    `;

    // Gráfico de Margens
    const ctxMargin = document.getElementById('marginChart').getContext('2d');
    new Chart(ctxMargin, {
        type: 'line',
        data: {
            labels: data.chartMargens.labels,
            datasets: [
                {
                    label: 'Margem Bruta (%)',
                    data: data.chartMargens.margemBruta,
                    borderColor: '#0AE18C',
                    backgroundColor: 'rgba(10, 225, 140, 0.1)',
                    fill: true,
                    tension: 0.4
                },
                {
                    label: 'Margem Líquida (%)',
                    data: data.chartMargens.margemLiquida,
                    borderColor: '#14C8FA',
                    backgroundColor: 'transparent',
                    borderDash: [5, 5],
                    tension: 0.4
                }
            ]
        },
        options: { responsive: true, maintainAspectRatio: false }
    });

    // Gráfico Não Operacional
    const ctxNonOp = document.getElementById('nonOpChart').getContext('2d');
    new Chart(ctxNonOp, {
        type: 'bar',
        data: {
            labels: data.chartNaoOperacional.labels,
            datasets: [{
                label: 'Impacto (R$)',
                data: data.chartNaoOperacional.data,
                backgroundColor: '#FF3131',
                borderRadius: 4
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false
        }
    });
});
