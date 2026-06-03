// js/api.js - Cliente API integrado ao Back-end (FastAPI)

const BASE_URL = 'http://localhost:8000/api';

const ApiService = {
    // Busca anos disponíveis
    getAnos: async () => {
        try {
            const response = await fetch(`${BASE_URL}/filtros/anos`);
            if (!response.ok) throw new Error('Erro ao buscar anos');
            return await response.json();
        } catch (error) {
            console.error(error);
            return [];
        }
    },

    // Busca empresas disponíveis
    getEmpresas: async () => {
        try {
            const response = await fetch(`${BASE_URL}/filtros/empresas`);
            if (!response.ok) throw new Error('Erro ao buscar empresas');
            return await response.json();
        } catch (error) {
            console.error(error);
            return [];
        }
    },
    // Busca dados reais do EBITDA via API
    getEbitdaData: async (ano = '', empresa = '') => {
        try {
            const queryParams = new URLSearchParams();
            if (ano) queryParams.append('ano', ano);
            if (empresa) queryParams.append('empresa', empresa);
            
            const response = await fetch(`${BASE_URL}/ebitda?${queryParams.toString()}`);
            if (!response.ok) throw new Error('Erro ao buscar dados de EBITDA');
            return await response.json();
        } catch (error) {
            console.error(error);
            return null; // Tratar melhor o erro na UI depois
        }
    },

    // Busca dados de Rentabilidade
    getRentabilidadeData: async (ano = '', empresa = '') => {
        try {
            const queryParams = new URLSearchParams();
            if (ano) queryParams.append('ano', ano);
            if (empresa) queryParams.append('empresa', empresa);

            const response = await fetch(`${BASE_URL}/rentabilidade?${queryParams.toString()}`);
            if (!response.ok) throw new Error('Erro ao buscar dados de Rentabilidade');
            return await response.json();
        } catch (error) {
            console.error(error);
            return null;
        }
    },

    // Busca dados de Custos
    getCustosData: async (ano = '', empresa = '') => {
        try {
            const queryParams = new URLSearchParams();
            if (ano) queryParams.append('ano', ano);
            if (empresa) queryParams.append('empresa', empresa);

            const response = await fetch(`${BASE_URL}/custos?${queryParams.toString()}`);
            if (!response.ok) throw new Error('Erro ao buscar dados de Custos');
            return await response.json();
        } catch (error) {
            console.error(error);
            return null;
        }
    }
};

window.ApiService = ApiService;
