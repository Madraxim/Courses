// drop hover start

let headerForm = document.querySelector('.header__form'),
    headerDropdownList = document.querySelector('.header__dropdown-list'),
    headerDropdownIcons = document.querySelector('.header__dropdown-icon'),
    headerDropIcon = document.querySelector('.header__drop-icon'),
    headerDropUserIcon = document.querySelector('.header__user-icon'),
    lessonsTitle = document.querySelector('.lessons__title'),
    main = document.querySelector('main');

headerForm.addEventListener('click', (e) => {
if(e.target.closest('.header__dropdown-icon')){
if (headerDropdownList.classList.contains('drop-active')){
                headerDropdownList.classList.remove('drop-active');
                main.style.filter = 'brightness(1)'
            } else{
                headerDropdownList.classList.toggle('drop-active');
                main.style.filter = 'brightness(0.3)'
                console.log(headerForm)
            }

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