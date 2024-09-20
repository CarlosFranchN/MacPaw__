let nav = document.querySelector('.nav')

const macPawLogo = document.querySelector('.nav-logo')
const logoSvg = document.querySelector('.icon-macpaw-paw-img')
const logoSvgPath = document.querySelector('.icon-macpaw-paw-img path')
const logoTextSvg = document.querySelector('.nav-links-text')
const logoTextSvgPath = document.querySelector('.icon-macpaw-text-svg path')

macPawLogo.addEventListener('mouseover', function () {
  console.log('Carlos')

  logoSvg.style.transition = 'transform 1s ease'
  logoSvg.style.transform = 'rotate(360deg)'
})
macPawLogo.addEventListener('mouseout', function () {
  logoSvg.style.transition = 'transform 1s ease'
  logoSvg.style.transform = 'rotate(-360deg)'
})

const divStoreSvg = document.querySelector('.divStoreIcon')
const storeSvg = document.querySelector('.store-icon')
divStoreSvg.addEventListener('mouseover', function () {
  storeSvg.style.transform = 'scale(1.35)'
  storeSvg.style.transition = 'transform 0.5s ease'
})
divStoreSvg.addEventListener('mouseout', function () {
  storeSvg.style.transform = 'scale(1)'
  storeSvg.style.transition = 'transform 0.5s ease'
})

const humbSvg = document.querySelector('.humb-img') // Corrigi para "humb-img"
// const humbSvgPath = document.querySelector('.humb-img') // Corrigi para "humb-img"

const humbBtn = document.querySelector('.humb')

humbBtn.addEventListener('mouseover', function () {
  if (humbSvg.getAttribute('value') === 'h') {
    humbSvg.style.transform = 'rotateY(360deg)'
    humbSvg.style.transition = 'transform .6s ease-in-out'
  }
})

humbBtn.addEventListener('mouseleave', function () {
  humbSvg.style.transform = 'rotateY(-0deg)'
  humbSvg.style.transition = 'transform .6s ease-in-out'
})


function menuToX(humb) {
  humb.setAttribute(
    'd',
    'M376.6 84.5c11.3-13.6 9.5-33.8-4.1-45.1s-33.8-9.5-45.1 4.1L192 206 56.6 43.5C45.3 29.9 25.1 28.1 11.5 39.4S-3.9 70.9 7.4 84.5L150.3 256 7.4 427.5c-11.3 13.6-9.5 33.8 4.1 45.1s33.8 9.5 45.1-4.1L192 306 327.4 468.5c11.3 13.6 31.5 15.4 45.1 4.1s15.4-31.5 4.1-45.1L233.7 256 376.6 84.5z'
  )
  humb.setAttribute('value', 'x')
}

function menuToH(humb) {
  humb.setAttribute(
    'd',
    "M0 96C0 78.3 14.3 64 32 64l384 0c17.7 0 32 14.3 32 32s-14.3 32-32 32L32 128C14.3 128 0 113.7 0 96zM0 256c0-17.7 14.3-32 32-32l384 0c17.7 0 32 14.3 32 32s-14.3 32-32 32L32 288c-17.7 0-32-14.3-32-32zM448 416c0 17.7-14.3 32-32 32L32 448c-17.7 0-32-14.3-32-32s14.3-32 32-32l384 0c17.7 0 32 14.3 32 32z"
  
  )
  humb.setAttribute('value', 'h')
}


humbBtn.addEventListener('click', () => {
  
  // Adiciona a classe '-open' ao menu de navegação
  if (humbSvg.getAttribute('value') === 'h') {
    humbSvg.style.transform = 'rotateX(90deg)'
    humbSvg.style.transition = 'transform .5s ease'
    nav.classList.add('-open')
  
    // Altera a cor do logo e dos textos para branco
    logoSvgPath.style.fill = 'white'
    logoTextSvgPath.style.fill = 'white'
    humbSvg.style.fill = 'white'
  
  
    humbBtn.style.color = 'white'
  
  
    setTimeout(() => {
      menuToX(humbSvg)
    }, 600);
    setTimeout(()=> {
      humbSvg.style.transform = 'rotateX(0deg)'
      humbSvg.style.transition = 'transform 0.5s ease'
      
    },500)
  

  }
  
})
humbBtn.addEventListener('click', () => {
  
  // Adiciona a classe '-open' ao menu de navegação
  if (humbSvg.getAttribute('value') === 'x') {
    humbSvg.style.transform = 'rotateX(90deg)'
    humbSvg.style.transition = 'transform .5s ease'
    nav.classList.remove('-open')
  
    // Altera a cor do logo e dos textos para branco
    logoSvgPath.style.fill = 'black'
    logoTextSvgPath.style.fill = 'black'
    humbSvg.style.fill = 'black'
  
  
    humbBtn.style.color = 'black'
  
  
    setTimeout(() => {
      menuToH(humbSvg)
    }, 600);
    setTimeout(()=> {
      humbSvg.style.transform = 'rotateX(0deg)'
      humbSvg.style.transition = 'transform 0.5s ease'
      
    },500)

  }})

  