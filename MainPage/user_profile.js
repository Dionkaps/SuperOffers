const editUsername = document.getElementById("edit_username");
const username_container = document.getElementById("username");

editUsername.addEventListener("click", function () {

    while (username_container.firstChild) {
        username_container.removeChild(username_container.firstChild);
      }

    const input = document.createElement("input");
    input.setAttribute("type", "text");
    input.setAttribute("id", "username_input");
    username_container.appendChild(input);
});


const editPassword = document.getElementById("edit_password");
const passwword_container = document.getElementById("password");

editPassword.addEventListener("click", function () {

    while (passwword_container.firstChild) {
        passwword_container.removeChild(passwword_container.firstChild);
      }

    const input = document.createElement("input");
    input.setAttribute("type", "text");
    input.setAttribute("id", "password_input");
    passwword_container.appendChild(input);
});
