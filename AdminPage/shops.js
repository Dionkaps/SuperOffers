function shopsAlert() {
    const formElement = document.forms["shopsForm"];

    const formData = new FormData(formElement);

    fetch("shopsJson.php", {
        method: "POST",
        body: formData,
    })
        .then((response) => response.text())
        .then((data) => {
            console.log("Server response:", data);

            if (data === "Insert") {
                alert("Shops inserted successfully!");
            } else {
                alert("Operation did not succeed.");
            }
        })
        .catch((error) => {
            console.error("Error:", error);
        });
}