// js/api.js - Mock API para simular os dados do Power BI

const ApiService = {
    // Dados para EBITDA
    getEbitdaData: async () => {
        // Simulação de delay de rede
        return new Promise(resolve => setTimeout(() => {
            resolve({
                kpis: {
                    receitaBruta: { value: 'R$ 14.5M', trend: '+2.4%', isPositive: true },
                    receitaLiquida: { value: 'R$ 12.1M', trend: '+1.8%', isPositive: true },
                    ebitda: { value: 'R$ 3.8M', trend: '+4.2%', isPositive: true },
                    margemEbitda: { value: '31.4%', trend: '-0.5p.p', isPositive: false }
                },
                chartEvolucao: {
                    labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
                    margem: [28, 29, 31, 30, 31, 31.4],
                    ebitda: [2.5, 2.8, 3.2, 3.1, 3.5, 3.8],
                    receita: [8.9, 9.6, 10.3, 10.3, 11.2, 12.1]
                },
                chartCascata: {
                    labels: ['Receita Líquida', 'CPV', 'Despesas ADM', 'Despesas COM', 'EBITDA'],
                    data: [12.1, -5.2, -1.8, -1.3, 3.8]
                }
            });
        }, 300));
    },

    // Dados para Rentabilidade
    getRentabilidadeData: async () => {
        return new Promise(resolve => setTimeout(() => {
            resolve({
                kpis: {
                    lucroBruto: { value: 'R$ 6.9M', trend: '+3.1%', isPositive: true },
                    margemBruta: { value: '57.0%', trend: '+1.2p.p', isPositive: true },
                    lucroLiquido: { value: 'R$ 2.4M', trend: '-1.5%', isPositive: false },
                    margemLiquida: { value: '19.8%', trend: '-0.8p.p', isPositive: false }
                },
                chartMargens: {
                    labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
                    margemBruta: [55, 56, 57, 56, 56.5, 57],
                    margemLiquida: [18, 19, 20.5, 20, 19.5, 19.8]
                },
                chartNaoOperacional: {
                    labels: ['Desp. Financeiras', 'Impostos', 'Outras Desp.'],
                    data: [-800000, -450000, -150000]
                }
            });
        }, 300));
    },

    // Dados para Custos
    getCustosData: async () => {
        return new Promise(resolve => setTimeout(() => {
            resolve({
                kpis: {
                    custoTotal: { value: 'R$ 5.2M', trend: '+4.5%', isPositive: false },
                    custoMedio: { value: 'R$ 1.250', trend: '-2.1%', isPositive: true },
                    percentualReceita: { value: '42.9%', trend: '+1.1p.p', isPositive: false }
                },
                chartGrupos: {
                    labels: ['Grupo A', 'Grupo B', 'Grupo C', 'Grupo D', 'Grupo E'],
                    atual: [1200, 1500, 800, 2100, 950],
                    anterior: [1150, 1550, 750, 1900, 1000]
                }
            });
        }, 300));
    }
};

window.ApiService = ApiService;
