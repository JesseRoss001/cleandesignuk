document.addEventListener("DOMContentLoaded", function(){
    const cookieConsent = localStorage.getItem('cookieConsent');

    if (!cookieConsent) {
        var cookieModal = new bootstrap.Modal(document.getElementById('cookieConsentModal'));
        cookieModal.show();
    }

    document.querySelector('#cookieConsentModal .btn-primary').addEventListener('click', function() {
        localStorage.setItem('cookieConsent', 'accepted');
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');

    navbarToggler.addEventListener('click', function () {
        navbarCollapse.classList.toggle('show');
    });

    // Optional: Close navbar when a link is clicked (useful for SPA or smooth scrolling)
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function () {
            if (navbarCollapse.classList.contains('show')) {
                navbarCollapse.classList.remove('show');
            }
        });
    });
});
