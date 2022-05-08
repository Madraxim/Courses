// drop hover start

let headerDropdownList = document.querySelector('.header__dropdown-list'),
    headerDropdownIcon = document.querySelector('.header__dropdown-icon'),
    headerDropdownIconAva = document.querySelector('.header__user-icon'),
    main = document.querySelector('main'),
    headerDrop = document.querySelector('.header__drop');

document.addEventListener('click', (e) => {
    if (e.target == headerDropdownIconAva || e.target == headerDrop || e.target == headerDropdownIcon) {
        headerDropdownList.classList.toggle('drop-active');
        headerDrop.classList.toggle('active');
    } else if (e.target == main) {
        headerDropdownList.classList.remove('drop-active');
        headerDrop.classList.remove('active');
    }
})


let hdeD = document.querySelector('.header__dropdown-extraDad'),
    dropItem = document.querySelectorAll('.dropdown-item'),
    hdeS = document.querySelector('.header__dropdown-extraSon'),
    headerAccount = document.querySelector('.header__account');

// drop hover end

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
    headerDropdown.classList.add('active');
})

bg.addEventListener('click', (e) => {
    nav.classList.remove('active');
    bg.classList.remove('active');
    body.classList.remove('lock');
    headerDropdown.classList.remove('active');
})

// burger end

// swipe start

let logo = document.querySelector('.logo');

logo.addEventListener('click', (e) => {
    e.preventDefault();
    nav.classList.remove('active');
    bg.classList.remove('active');
    body.classList.remove('lock');
})

// swipe end

// search start

let headerSearch = document.querySelector('.header__search'),
    modalSearch = document.querySelector('.modal-search'),
    modalPlus = document.querySelector('.modal-search__img-plus');

headerSearch.addEventListener('click', function (e) {
    modalSearch.classList.add('active');
    body.classList.add('lock');
})

modalPlus.addEventListener('click', function (e) {
    modalSearch.classList.remove('active');
    body.classList.remove('lock');
})

// search end