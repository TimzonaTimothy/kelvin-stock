window.addEventListener('load', (event) => {
    let preloader = document.querySelector('.preloader')
    setTimeout(() => {
        preloader.classList.add('transition-all')
        preloader.classList.add('duration-500')
        preloader.classList.add('invisible')
        preloader.classList.add('!opacity-0')
    }, 100)
});

// Mobile Menu
let menuWrapper = document.querySelector('.menu-wrapper')
let menuBox = document.querySelector('.menu-box')
let menuClose = document.querySelector('#menu-close')
let menuOpen = document.querySelector('.menu-open')

function openMenu(){
    menuWrapper.classList.add('!opacity-100')
    menuWrapper.classList.add('!visible')
    menuBox.classList.add('!left-0')
}

function closeMenu(){
    menuWrapper.classList.remove('!opacity-100')
    menuWrapper.classList.remove('!visible')
    menuBox.classList.remove('!left-0')
}
menuOpen.addEventListener('click', openMenu)

menuClose.addEventListener('click', closeMenu)
// Mobile Menu end

// Search box modal
let searchWrapper = document.querySelector(".search-wrapper")
let searchBox = document.querySelector(".search-box")
let openSearchbars = document.querySelectorAll('.open-search')
let searchClose = document.querySelector("#search-close")

function openSearch() {
    searchBox.classList.add("!mt-0")
    searchWrapper.classList.add("!visible")
    searchWrapper.classList.add("!opacity-100")
}

function closeSearch() {
    searchBox.classList.remove("!mt-0")
    searchWrapper.classList.remove("!visible")
    searchWrapper.classList.remove("!opacity-100")
}

for (let openSearchbar of openSearchbars) {
    openSearchbar.addEventListener("click", openSearch)
}

searchClose.addEventListener("click", closeSearch)
document.addEventListener('keyup', function (e) {
    if (e.keyCode === 27) {
        closeSearch()
    }
    if (e.ctrlKey && e.keyCode === 75) {
        openSearch()
    }
})
// Search modal end

// Shopping cart
let cartWrapper = document.querySelector('.cart-wrapper')
let cartBox = document.querySelector('#cart-box')
let cartClose = document.querySelector('#cart-close')
let cartOpens = document.querySelectorAll('.cart-open')

for (cartOpen of cartOpens) {
    cartOpen.addEventListener('click', function () {
        cartWrapper.classList.add('!opacity-100')
        cartWrapper.classList.add('!visible')
        cartBox.classList.add('!right-0')
    })
}

// cartClose.addEventListener('click', closeCart)

function closeCart() {
    cartWrapper.classList.remove('!opacity-100')
    cartWrapper.classList.remove('!visible')
    cartBox.classList.remove('!right-0')
}
// Shopping cart end

// Global
document.addEventListener('click', function (e) {
    // close cart
    if (e.target.classList.contains('cart-wrapper')) {
        closeCart()
    }
    // Close search
    if(e.target.classList.contains('search-wrapper')){
        closeSearch()
    }
    // Close menu
    if(e.target.classList.contains('menu-wrapper')){
        closeMenu()
    }
})
