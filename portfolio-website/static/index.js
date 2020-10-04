const navToogle = document.querySelector('.nav-toggle');

navToogle.addEventListener('click', () => {
    document.body.classList.toggle('nav-open');
});