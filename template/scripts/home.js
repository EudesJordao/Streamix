   const carrossel = document.getElementById('carrossel');
    const setaEsquerda = document.querySelector('.seta.esquerda');
    const setaDireita = document.querySelector('.seta.direita');

    const scrollAmount = 4 * 195;

    setaEsquerda.addEventListener('click', () => {
        carrossel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    });

    setaDireita.addEventListener('click', () => {
        carrossel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    });

    // Imagem popup
    const popup = document.getElementById('popup');
    const popupImg = document.getElementById('popup-img');
    const fecharBtn = document.querySelector('.fechar');

    document.querySelectorAll('.carrossel img').forEach(img => {
        img.addEventListener('click', () => {
            popupImg.src = img.src;
            popup.style.display = 'block';
        });
    });

    fecharBtn.addEventListener('click', () => {
        popup.style.display = 'none';
        popupImg.src = '';
    });

    // Fechar ao clicar fora da imagem
    popup.addEventListener('click', (e) => {
        if (e.target === popup) {
            popup.style.display = 'none';
            popupImg.src = '';
        }
    });
