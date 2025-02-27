// Animação de fade in ao carregar a página
document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('.alert, .caixa');
    elements.forEach(element => {
        element.style.opacity = 0;
        element.style.transition = 'opacity 0.5s';
        element.style.opacity = 1;
    });
});
