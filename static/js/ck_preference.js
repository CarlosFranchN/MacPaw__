const btn_close = document.querySelector(".cky-btn-close");
const modal = document.querySelector(".cky-modal")
// Adiciona o listener para o evento de clique
btn_close.addEventListener("click", function() {
  modal.classList.remove("cky-modal-open")
  const overlay = document.querySelector(".cky-overlay")
  overlay.classList.add("cky-hide")
  console.log("Removido");
  
});

document.querySelector('.lang-switcher__select').addEventListener('change', function() {
  const selectedLanguage = this.value;
  const links = document.querySelectorAll('.lang-switcher__link');

  
  links.forEach(link => {
      if (link.getAttribute('data-switcher-id') === selectedLanguage) {
          window.location.href = link.getAttribute('href');
      }
  });
});
