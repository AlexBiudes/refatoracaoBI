// js/app.js - Lógica comum da interface

document.addEventListener('DOMContentLoaded', async () => {
    // Animação inicial suave
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    }, 50);

    // Lógica de Troca de Tema
    const themeToggleBtn = document.getElementById('theme-toggle');
    
    const applyTheme = (theme) => {
        if (theme === 'light') {
            document.documentElement.setAttribute('data-theme', 'light');
            if (themeToggleBtn) themeToggleBtn.textContent = '🌑'; // Lua Nova/Dark mode icon
        } else {
            document.documentElement.removeAttribute('data-theme');
            if (themeToggleBtn) themeToggleBtn.textContent = '☀️'; // Sol/Light mode icon
        }
    };

    // Inicializar tema pelo localStorage (default dark)
    const savedTheme = localStorage.getItem('planning_theme') || 'dark';
    applyTheme(savedTheme);

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            localStorage.setItem('planning_theme', newTheme);
            applyTheme(newTheme);
        });
    }

    const selectAno = document.getElementById('filter-ano');
    const selectEmpresa = document.getElementById('filter-empresa');

    // Função com Retry (Polling) para aguardar o Backend iniciar
    const waitForData = async (fetchFunction) => {
        let data = [];
        while (!data || data.length === 0) {
            data = await fetchFunction();
            if (!data || data.length === 0) {
                // Se a API ainda não tiver subido, espera 1 segundo e tenta de novo
                await new Promise(resolve => setTimeout(resolve, 1000));
            }
        }
        return data;
    };

    if (selectAno && selectEmpresa) {
        const savedAno = localStorage.getItem('planning_filter_ano');
        const savedEmpresa = localStorage.getItem('planning_filter_empresa');

        // Aguarda os dados do backend ficarem prontos!
        const anos = await waitForData(window.ApiService.getAnos);
        const empresas = await waitForData(window.ApiService.getEmpresas);
        if (anos && anos.length > 0) {
            selectAno.innerHTML = '';
            anos.forEach(ano => {
                const opt = document.createElement('option');
                opt.value = ano;
                opt.textContent = `Ano: ${ano}`;
                selectAno.appendChild(opt);
            });
            if (savedAno && anos.map(String).includes(savedAno)) {
                selectAno.value = savedAno;
            }
        } else {
            console.error("Nenhum ano retornado pela API. O backend está rodando?");
        }

        // Buscar empresas
        if (empresas && empresas.length > 0) {
            selectEmpresa.innerHTML = '<option value="">Empresa: Todas</option>';
            empresas.forEach(emp => {
                const opt = document.createElement('option');
                opt.value = emp;
                opt.textContent = emp;
                selectEmpresa.appendChild(opt);
            });
            if (savedEmpresa && empresas.includes(savedEmpresa)) {
                selectEmpresa.value = savedEmpresa;
            }
        } else {
            console.error("Nenhuma empresa retornada pela API.");
        }

        // Listener de eventos para recarregar a tela
        const dispatchChange = () => {
            localStorage.setItem('planning_filter_ano', selectAno.value);
            localStorage.setItem('planning_filter_empresa', selectEmpresa.value);
            
            const event = new CustomEvent('filtersChanged', {
                detail: { ano: selectAno.value, empresa: selectEmpresa.value }
            });
            document.dispatchEvent(event);
        };

        selectAno.addEventListener('change', dispatchChange);
        selectEmpresa.addEventListener('change', dispatchChange);

        // Dispara primeiro evento para renderizar com os filtros iniciais
        dispatchChange();
        
        // Remove a tela de carregamento (Spinner) e revela o dashboard!
        const loader = document.getElementById('global-loader');
        if (loader) loader.classList.add('hidden');
        document.body.style.opacity = '1';
    } else {
        document.body.style.opacity = '1';
    }
});

// Funções utilitárias globais
const formatCurrency = (value) => {
    return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value);
};
