// js/app.js - Lógica comum da interface

document.addEventListener('DOMContentLoaded', async () => {
    // Animação inicial suave
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    }, 50);

    const selectAno = document.getElementById('filter-ano');
    const selectEmpresa = document.getElementById('filter-empresa');

    if (selectAno && selectEmpresa) {
        // Buscar anos
        const anos = await window.ApiService.getAnos();
        if (anos && anos.length > 0) {
            selectAno.innerHTML = '';
            anos.forEach(ano => {
                const opt = document.createElement('option');
                opt.value = ano;
                opt.textContent = `Ano: ${ano}`;
                selectAno.appendChild(opt);
            });
            // O primeiro ano já vem selecionado por padrão
        }

        // Buscar empresas
        const empresas = await window.ApiService.getEmpresas();
        if (empresas && empresas.length > 0) {
            selectEmpresa.innerHTML = '<option value="">Empresa: Todas</option>';
            empresas.forEach(emp => {
                const opt = document.createElement('option');
                opt.value = emp;
                opt.textContent = emp;
                selectEmpresa.appendChild(opt);
            });
        }

        // Listener de eventos para recarregar a tela
        const dispatchChange = () => {
            const event = new CustomEvent('filtersChanged', {
                detail: { ano: selectAno.value, empresa: selectEmpresa.value }
            });
            document.dispatchEvent(event);
        };

        selectAno.addEventListener('change', dispatchChange);
        selectEmpresa.addEventListener('change', dispatchChange);

        // Dispara primeiro evento para renderizar com os filtros iniciais
        dispatchChange();
    }
});

// Funções utilitárias globais
const formatCurrency = (value) => {
    return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value);
};
