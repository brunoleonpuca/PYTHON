(function ($) {
    "use strict"; //Start use of strict

    // Closes responsive menu when a scroll trigger link is clicked
    $(".js-scroll-trigger").click(function () {
        $(".navbar-collapse").collapse("hide");
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $("body").scrollspy({
        target: "#main-nav",
        offset: 74
    });

    // Collapse Navbar
    var navbarCollapse = function () {
        if ($("#main-nav").offset().top > 100) {
            $("#main-nav").addClass("navbar-shrink");
        } else {
            $("#main-nav").removeClass("navbar-shrink");
        }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);


})(jQuery); //End use of strict