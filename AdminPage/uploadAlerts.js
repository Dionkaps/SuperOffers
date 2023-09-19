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

function deleteProductsData() {
    if (confirm("Are you sure you want to delete all data from the 'products' table?")) {
        fetch("deleteProducts.php", {
            method: "POST",
        })
            .then((response) => response.text())
            .then((data) => {
                console.log("Server response:", data);

                if (data === "Success") {
                    alert("All data from the 'products' table has been deleted.");
                } else {
                    alert("Deletion operation did not succeed.");
                }
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }
}
document.addEventListener("DOMContentLoaded", function () {
  const deleteButton = document.getElementById("deleteButton");
  const messageDiv = document.getElementById("message");

  deleteButton.addEventListener("click", function () {
      
      const xhr = new XMLHttpRequest();
      xhr.open("POST", "deleteProducts.php", true);
      xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

      xhr.onreadystatechange = function () {
          if (xhr.readyState === 4 && xhr.status === 200) {
              // Display the response from the PHP script in the messageDiv
              messageDiv.textContent = xhr.responseText;
          }
      };

      xhr.send();
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const deleteShopsButton = document.getElementById("deleteShopsButton");
  const messageDiv = document.getElementById("message");
deleteShopsButton.addEventListener("click", function() {
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "deleteShops.php", true);
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

  xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
          // Display the response from the PHP script in the messageDiv
          messageDiv.textContent = xhr.responseText;
      }
  };

  xhr.send();
});
});