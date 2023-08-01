//Set the width of the side navigation to 250px for screens larger than or equal to 1121px
function openNav() {
  if (window.innerWidth >= 1121) {
    document.getElementById("buttonContainer").style.width = "12%";
  } else if (window.innerWidth < 1121) {
    document.getElementById("buttonContainer").style.width = "100%";
    document.getElementById("buttonContainer").style.height = "200vh";
  }
}

//Set the width of the side navigation to 0
function closeNav() {
  document.getElementById("buttonContainer").style.width = "0";
}

window.addEventListener("resize", function () {
  if (window.matchMedia("(min-width: 1121px)").matches) {
    closeNav();
  } else {
    
  }
});
