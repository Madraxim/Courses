// burger start

let nav = document.querySelector('.nav'),
    iconBurger = document.querySelector('.fal.fa-bars'),
    body = document.querySelector('body'),
    headerDropdown = document.querySelector('.header__dropdown'),
    lessVideo = document.querySelector('.lesson__video'),
    bg = document.querySelector('.bg');

iconBurger.addEventListener('click', (e) => {
    nav.classList.add('active');
    bg.classList.add('active');
    body.classList.add('lock');
})

bg.addEventListener('click', (e) => {
    nav.classList.remove('active');
    bg.classList.remove('active');
    body.classList.remove('lock');
})

// burger end

// swipe start

let logo = document.querySelector('.logo');

logo.addEventListener('click', (e) =>{
    e.preventDefault();
    nav.classList.remove('active');
    bg.classList.remove('active');
    body.classList.remove('lock');
})

// swipe end