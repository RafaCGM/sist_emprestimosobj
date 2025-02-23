/*===== SCROLL REVEAL ANIMATION =====*/

document.addEventListener('DOMContentLoaded', function() {
    const sr = ScrollReveal({
        distance: '60px',
        duration: 2000,
        delay: 200,
        reset: true  // Ativar se eu quiser que os elementos revelem novamente ao rolar
    });

    // Configurações para diferentes elementos
    sr.reveal('.home_titulo, .home_subtitulo', {
        origin: 'top'
    });

    sr.reveal ('.home_opcoes', {
        origin: 'bottom',
        interval: 200 
    })

    sr.reveal ('.',{
        origin: 'right',
        interval: 200
    })

    sr.reveal ('.',{
        origin: 'left',
        interval: 200
    })

    sr.reveal('.', {
        origin: 'right',
        delay: 400
    });

    sr.reveal('.', {
        origin: 'bottom',
        delay: 400
    });

    sr.reveal('', {
        origin: 'left',
        delay: 400
    });

    sr.reveal('.emprestimo_card', {
        interval: 16,  // Intervalo de 16ms entre as animações
        origin: 'bottom',  // A animação vai ocorrer de baixo para cima (pode ajustar conforme necessidade)
        distance: '50px',  // A distância que o elemento irá se mover
        duration: 1500,  // Duração da animação (em milissegundos)

    });

});
