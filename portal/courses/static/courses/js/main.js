// dropdown start
let navExtra = document.querySelector('.nav__extra'),
    navPlus = document.querySelector('.nav__plus'),
    navList = document.querySelector('.nav__list');

navExtra.addEventListener('click', (e) => {
    if (navList.classList.contains('active')){
        navPlus.innerHTML = '+';
        navList.classList.remove('active');
    } else {
        navList.classList.add('active');
        navPlus.innerHTML = '-';
    }
})
// dropdown end

// drop hover start

let headerDropdownList = document.querySelector('.header__dropdown-list'),
    headerDropdownIcon = document.querySelector('.header__dropdown-icon'),
    headerDropdownIconAva = document.querySelector('.header__user-icon'),
    lessonInfo = document.querySelector('.lesson__info'),
    lesson = document.querySelector('.lesson'),
    headerDrop = document.querySelector('.header__drop-icon');

addEventListener('click', (e) => {
    if (e.target == headerDrop || e.target == headerDropdownIcon || e.target == headerDropdownIconAva) {
        headerDropdownList.classList.toggle('drop-active');
        headerDrop.classList.toggle('active');
    } else if (e.target == lesson || e.target == lessonInfo) {
        headerDropdownList.classList.remove('drop-active');
        headerDrop.classList.remove('active');
    }
})


let hdeD = document.querySelector('.header__dropdown-extraDad'),
    dropItem = document.querySelectorAll('.dropdown-item .linkName'),
    hdeS = document.querySelectorAll('.header__dropdown-extraSon'),
    dropdownItemLink = document.querySelector('.dropdown-itemLink');
    for (let i = 0; i < dropItem.length; i++) {
        dropItem[i].addEventListener('click', (e) => {
            if (hdeS[i].style['display'] == 'inline-block'){
                hdeS[i].style['display'] = 'none';
            } else {
                for (let j = 0; j < hdeS; j++) {
                    hdeS[i].style['display'] = 'none';
                }
                hdeS[i].style['display'] = 'inline-block';
            }
        })
    }

// drop hover end


// desc tabs start

//let descTab = document.querySelectorAll('.description__tab'),
//    descItem = document.querySelectorAll('.description__item');
//
//descItem.forEach((el, i) => {
//    el.addEventListener('click', function (e) {
//        descItem.forEach((el, k) => {
//            e.preventDefault();
//            el.classList.remove('active');
//            descTab[k].classList.remove('active');
//        });
//        this.classList.add('active');
//        descTab[i].classList.add('active');
//    })
//});

// desc tabs end

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
    lessVideo.classList.add('active');
})

bg.addEventListener('click', (e) => {
    nav.classList.remove('active');
    bg.classList.remove('active');
    body.classList.remove('lock');
    headerDropdown.classList.remove('active');
    lessVideo.classList.remove('active');
})

// burger end

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