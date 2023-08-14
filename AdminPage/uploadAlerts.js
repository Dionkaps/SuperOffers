function productsAlert() {
  const formElement = document.forms["productsForm"];

  const formData = new FormData(formElement);

  fetch("productsJson.php", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.text())
    .then((data) => {
      console.log("Server response:", data);

      if (data === "Insert") {
        alert("Products inserted successfully!");
      } else if (data === "Update") {
        alert("Products updated successfully!");
      } else {
        alert("Operation did not succeed.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function pricesAlert() {
  const formElement = document.forms["pricesForm"];

  const formData = new FormData(formElement);

  fetch("pricesJson.php", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.text())
    .then((data) => {
      console.log("Server response:", data);

      if (data === "Insert") {
        alert("Prices inserted successfully!");
      } else {
        alert("Operation did not succeed.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
