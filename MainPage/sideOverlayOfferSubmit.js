function openFullNav() {
    if (window.innerWidth >= 1121) {
        document.getElementById("mySidenav").style.width = "100%";
    } else if (window.innerWidth < 1121) {
        document.getElementById("mySidenav").style.width = "100%";
        document.getElementById("mySidenav").style.height = "200vh";
    }
}

function closeFullNav() {
    document.getElementById("mySidenav").style.width = "0";
}

window.addEventListener("resize", function () {
    if (window.matchMedia("(min-width: 1121px)").matches) {
        closeFullNav();
    } else {

    }
});