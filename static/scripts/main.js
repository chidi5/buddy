document.addEventListener('DOMContentLoaded', () => {
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.nav-link'), 0);

    if ($navbarBurgers.length > 0) {
        $navbarBurgers.forEach( el => {
            el.addEventListener('click', () => {
                const target = el.dataset.target;
                const $target = document.getElementById(target);

                $( '.navbar-nav' ).find( 'a.active' ).removeClass( 'active' );
                el.classList.toggle('active');
                $target.classList.toggle('active');
            });
        });
    }
});
