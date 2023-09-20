function checkDataFromPHP() {
  const formElement = document.forms["signInForm"];

  //Create a new FormData object and append the form data to it
  const formData = new FormData(formElement);

  fetch("adminSignin.php", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.text())
    .then((data) => {

      //Check server the response and display the result
      if (data === "Correct") {
        window.location.href = "../AdminPage/AdminPage.html";
      } else if (data === "Wrong") {
        alert("Wrong credentials. Try again!");
      } else {
        alert("Unexpected response from server.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
