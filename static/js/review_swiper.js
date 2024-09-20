const review_btns = document.querySelectorAll('.reviews-btn')
const swiper_slides = document.querySelectorAll('.swiper-slide')
const slide_active = document.querySelector('.swiper-slide.-active')
const swiper_wrapper = document.querySelector("#swiper-wrapper-88b2c741090d7e1df")


let currentIndex = 0;
let isDragging = false;
let startPos = 0;
let currentTranslate = 0;
let prevTranslate = 0;
let animationID;


const slideWidth = swiper_slides[0].offsetWidth; // Assumindo que todos os slides têm a mesma largura

review_btns.forEach((btn, index) => {
    btn.addEventListener('click', function() {
        // Alterar classe ativa do botão
        review_btns.forEach(b => b.classList.remove('-active'));
        this.classList.add('-active');

        // Mover slides
        const offset = slideWidth * index;
        swiper_wrapper.style.transition = 'transform 0.5s ease-in-out';
        swiper_wrapper.style.transform = `translateX(-${offset}px)`;

        // Após a transição, atualizar classe ativa do slide
        swiper_wrapper.addEventListener('transitionend', () => {
            swiper_slides.forEach(slide => slide.classList.remove('-active'));
            swiper_slides[index].classList.add('-active');
        });

        // Atualizar o índice atual
        currentIndex = index;
    });
});
swiper_wrapper.addEventListener('mousedown', startDrag);
swiper_wrapper.addEventListener('touchstart', startDrag);

swiper_wrapper.addEventListener('mouseup', endDrag);
swiper_wrapper.addEventListener('mouseleave', endDrag);
swiper_wrapper.addEventListener('touchend', endDrag);
swiper_wrapper.addEventListener('touchcancel', endDrag);

swiper_wrapper.addEventListener('mousemove', drag);
swiper_wrapper.addEventListener('touchmove', drag);

function startDrag(event) {
    isDragging = true;
    startPos = getPositionX(event);
    animationID = requestAnimationFrame(animation);
    swiper_wrapper.style.transition = 'none';
}

function endDrag() {
    isDragging = false;
    cancelAnimationFrame(animationID);
    const movedBy = currentTranslate - prevTranslate;

    if (movedBy < -100 && currentIndex < swiper_slides.length - 1) {
        currentIndex += 1;
    }

    if (movedBy > 100 && currentIndex > 0) {
        currentIndex -= 1;
    }

    setPositionByIndex();
}

function drag(event) {
    if (isDragging) {
        const currentPosition = getPositionX(event);
        currentTranslate = prevTranslate + currentPosition - startPos;
    }
}

function getPositionX(event) {
    return event.type.includes('mouse') ? event.pageX : event.touches[0].clientX;
}

function animation() {
    setSliderPosition();
    if (isDragging) requestAnimationFrame(animation);
}

function setSliderPosition() {
    swiper_wrapper.style.transform = `translateX(${currentTranslate}px)`;
}

function setPositionByIndex() {
    currentTranslate = currentIndex * -slideWidth;
    prevTranslate = currentTranslate;
    swiper_wrapper.style.transition = 'transform 0.5s ease-in-out';
    swiper_wrapper.style.transform = `translateX(${currentTranslate}px)`;

    review_btns.forEach(b => b.classList.remove('-active'));
    review_btns[currentIndex].classList.add('-active');
}