// search start

let headerSearch = document.querySelector('.header__search'),
    modalSearch = document.querySelector('.modal-search'),
    modalPlus = document.querySelector('.modal-search__img-plus'),
    body = document.querySelector('body');



headerSearch.addEventListener('click', function (e) {
    modalSearch.classList.add('active');
    body.classList.add('lock');
})

modalPlus.addEventListener('click', function (e) {
    modalSearch.classList.remove('active');
    body.classList.remove('lock');
})

// search end