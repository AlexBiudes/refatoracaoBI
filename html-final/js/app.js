// js/app.js - Lógica comum da interface

document.addEventListener('DOMContentLoaded', () => {
    // Lógica para dropdowns e filtros comuns
    const dropdowns = document.querySelectorAll('.filter-dropdown');
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('change', (e) => {
            console.log(`Filtro alterado: ${e.target.value}`);
            // Aqui seria disparado um evento global ou re-fetch da API
            // alert(`Filtro aplicado: ${e.target.value}`);
        });
    });

    // Animação inicial suave
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    }, 50);
});

// Funções utilitárias globais
const formatCurrency = (value) => {
    return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value);
};
