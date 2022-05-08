// dropdown start
let navExtra = document.querySelector('.nav__extra'),
    navPlus = document.querySelector('.nav__plus'),
    navList = document.querySelector('.nav__list');

navExtra.addEventListener('click', (e) => {
    navList.classList.toggle('active');
    navPlus.innerText == '+' ? navPlus.innerText = '-' : navPlus.innerText = '+';
})
// dropdown end

// burger start

let nav = document.querySelector('.nav'),
    iconBurger = document.querySelector('.fal.fa-bars'),
    headerDropdown = document.querySelector('.header__dropdown'),
    bg = document.querySelector('.bg');

iconBurger.addEventListener('click', (e) => {
    nav.classList.add('active');
    bg.classList.add('active');
    body.classList.add('lock');
    headerDropdown.classList.add('active');
})

bg.addEventListener('click', (e) => {
    nav.classList.remove('active');
    bg.classList.remove('active');
    body.classList.remove('lock');
    headerDropdown.classList.remove('active');
})

// burger end