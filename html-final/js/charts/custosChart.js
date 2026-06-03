// js/charts/custosChart.js

let chartCostGroupInstance = null;

const renderCustos = async (ano, empresa) => {
    const kpiContainer = document.getElementById('kpi-container');
    kpiContainer.innerHTML = `<div style="text-align: center; width: 100%; padding: 40px; color: var(--primary-color); font-size: 1.2rem;">Carregando dados ao vivo do BigQuery... <br> <small style="color:var(--text-secondary);font-size:0.9rem;">Consultando milhões de linhas via Storage API.</small></div>`;
    
    // Buscar dados reais
    const data = await window.ApiService.getCustosData(ano, empresa);

    if (!data || data.error) {
        kpiContainer.innerHTML = `<div style="text-align: center; width: 100%; padding: 40px; color: #FF3131; font-size: 1.2rem;">Erro ao carregar dados: ${data?.error || 'Erro desconhecido'}</div>`;
        return;
    }

    // Renderizar KPIs
    const { custoTotal, custoMedio, percentualReceita } = data.kpis;
    
    kpiContainer.innerHTML = `
        <div class="kpi-card">
            <div class="kpi-title">Custo Total (Ano Atual)</div>
            <div class="kpi-value">${custoTotal.value}</div>
            <div class="kpi-trend ${custoTotal.isPositive ? 'positive' : 'negative'}">${custoTotal.trend} vs ano anterior</div>
        </div>
        <div class="kpi-card highlight-card">
            <div class="kpi-title">Custo Médio por Produto</div>
            <div class="kpi-value">${custoMedio.value}</div>
            <div class="kpi-trend ${custoMedio.isPositive ? 'positive' : 'negative'}">${custoMedio.trend} vs ano anterior</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">% Custos sobre Receita</div>
            <div class="kpi-value">${percentualReceita.value}</div>
            <div class="kpi-trend ${percentualReceita.isPositive ? 'positive' : 'negative'}">${percentualReceita.trend} vs ano anterior</div>
        </div>
    `;

    if (chartCostGroupInstance) chartCostGroupInstance.destroy();

    // Gráfico de Grupos de Custo
    const ctxCostGroup = document.getElementById('costGroupChart').getContext('2d');
    chartCostGroupInstance = new Chart(ctxCostGroup, {
        type: 'bar',
        data: {
            labels: data.chartGrupos.labels,
            datasets: [
                {
                    label: 'Ano Atual',
                    data: data.chartGrupos.atual,
                    backgroundColor: '#14C8FA',
                    borderRadius: 4
                },
                {
                    label: 'Ano Anterior',
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
};

document.addEventListener('filtersChanged', (e) => {
    const { ano, empresa } = e.detail;
    renderCustos(ano, empresa);
});
