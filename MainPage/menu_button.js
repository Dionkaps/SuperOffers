const menu = document.querySelector(".menu")
    const userstuff = document.querySelector(".userstuff")

    menu.addEventListener("click", () => {
      userstuff.classList.toggle('full_screen_menu')
    })