document.addEventListener('DOMContentLoaded', function () {
  const revisitBtn = document.querySelector('.cky-btn-revisit')
  console.log(revisitBtn)

  if (revisitBtn) {
    revisitBtn.addEventListener('click', function () {
      const modal = document.querySelector(".cky-modal")
      const overlay = document.querySelector(".cky-overlay")
      modal.classList.add("cky-modal-open")
      overlay.classList.remove("cky-hide")
    })
  } else {
    console.log('Carlos was here')
  }
})
