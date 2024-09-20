// Seleciona a div que deve aparecer
const myDiv = document.querySelector('.fixed-nav');

// Define o ponto da página onde a div deve aparecer
const showPoint = 300; // Ponto de rolagem em pixels

// Função para verificar a rolagem da página
function checkScroll() {
  if (window.scrollY >= showPoint) {
    myDiv.classList.add('-active');

  } else {

    myDiv.classList.remove('-active');
  }
}

// Adiciona o evento de rolagem para verificar a posição da página
window.onscroll = function() {
  checkScroll();
};
