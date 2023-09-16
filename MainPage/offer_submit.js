var popupWindow = document.getElementById("popup-window");
var closeButton = document.getElementById("close-button");
var prodName;
var newPrice;
var prodExists;
var oldPrice;

// Hide the pop-up window when the close button is clicked
closeButton.addEventListener("click", function () {
  popupWindow.style.display = "none";
});

//Dimiourgia methodou gia eisagwgi neas timis gia offer gia simplirwsi kritiriwn xristi gia na mporei na anevazei nea timi
function newOfferPrice(form) {
  newPrice = document.getElementById("newPrice").value;
  if (newPrice != 0 && newPrice != null && newPrice != "") {
    document.getElementById("superIdInput").value = superId;
    document.getElementById("productNameInput").value = prodName;
    if (prodExists) {
      console.log("newPrice: " + newPrice);
      console.log("oldPrice: " + oldPrice);
      if (newPrice < 0.8 * oldPrice) {
        var values = {
          spid: superId,
          pname: prodName,
        };
        fetch("deletePrevOffer.php", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(values),
        })
          .then((response) => response.text())
          .then((result) => {
            console.log(result);
          });
        form.action = "newPriceSubmit.php";
        form.submit();
        alert("Offer added successfully");
      } else {
        alert("Offer already exists");
      }
    } else {
      form.action = "newPriceSubmit.php";
      form.submit();
      alert("Offer added successfully");
    }
  } else {
    console.log(newPrice);
    alert("Please enter a valid price");
    document.getElementById("newPrice").value = "";
  }
}
const productGrid = document.querySelector(".product-grid");
const categoryDropdown = document.getElementById("categories");
const subcategoryDropdown = document.getElementById("subcategories");
const searchBox = document.getElementById("searchBox");
function productGridReset() {
  productGrid.innerHTML = ""; // Clear existing content
}

document.addEventListener("DOMContentLoaded", function () {
  //Searchbar

  searchBox.addEventListener("input", function () {
    const inputValue = searchBox.value.trim();

    if (inputValue.length >= 2) {
      fetch("fetchProductOnSearch.php?searchedName=" + inputValue)
        .then((response) => response.json())
        .then((data) => {
          productGridReset();

          data.forEach((product) => {
            const productItem = document.createElement("div");
            productItem.classList.add("product-item");

            const image = document.createElement("img");
            image.src = "/web/imgScript/" + product.image;
            image.alt = product.name;

            const name = document.createElement("p");
            name.textContent = product.name;

            const submitButton = document.createElement("button");
            submitButton.classList.add("submit-button");
            submitButton.textContent = "Add new offer";
            submitButton.addEventListener("click", function (event) {
              event.preventDefault();
              popupWindow.style.display = "block";
              prodExists = false;
              if (products.includes(product.name)) {
                prodExists = true;
                var values = {
                  spid: superId,
                  pname: product.name,
                };
                fetch("fetchOfferPrice.php", {
                  method: "POST",
                  headers: {
                    "Content-Type": "application/json",
                  },
                  body: JSON.stringify(values),
                })
                  .then((response) => response.text())
                  .then((result) => {
                    oldPrice = result;
                  });
              }
              prodName = product.name;
              console.log(products);
            });

            const productInfo = document.createElement("div");
            productInfo.classList.add("product-info");

            productItem.appendChild(image);
            productItem.appendChild(name);
            productItem.appendChild(submitButton);
            productGrid.appendChild(productItem);
          });
        });
    } else {
      productGridReset();
    }
  });

  // Function to populate dropdowns
  function populateDropdown(dropdown, data, dispText) {
    const first_option = document.createElement("option");
    first_option.textContent = dispText;

    dropdown.appendChild(first_option);
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.id;
      option.textContent = item.name;
      dropdown.appendChild(option);
    });
  }

  //Options for display text(dispText)
  catDispText = "Select a category";
  subcatDispText = "Select a subcategory";

  // Fetch categories and subcategories using XMLHttpRequest
  const xhr = new XMLHttpRequest();
  xhr.open("GET", "fetchCategoriesSubcategories.php", true); // Replace with the correct path to your JSON file
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      const data = JSON.parse(xhr.responseText);
      populateDropdown(categoryDropdown, data.categories, catDispText);

      // Event listener for category dropdown change
      categoryDropdown.addEventListener("change", function () {
        productGridReset();
        const selectedCategoryId = categoryDropdown.value;
        const category = data.categories.find(
          (category) => category.id === selectedCategoryId
        );
        subcategoryDropdown.innerHTML = ""; // Clear existing options
        if (category) {
          populateDropdown(
            subcategoryDropdown,
            category.subcategories,
            subcatDispText
          );
        }
      });
      subcategoryDropdown.addEventListener("change", function () {
        const selectedSubcategoryId = subcategoryDropdown.value;
        console.log(selectedSubcategoryId);

        //Fetch product data from selection
        const productGrid = document.querySelector(".product-grid");

        //Clear the existing content of the grid
        productGridReset();

        const xhrProduct = new XMLHttpRequest();
        xhrProduct.open(
          "GET",
          `fetchProductData.php?subcategory=${selectedSubcategoryId}`,
          true
        );
        xhrProduct.onreadystatechange = function () {
          if (xhrProduct.readyState === XMLHttpRequest.DONE) {
            if (xhrProduct.status === 200) {
              const productData = JSON.parse(xhrProduct.responseText);
              productData.forEach((product) => {
                const productItem = document.createElement("div");
                productItem.classList.add("product-item");

                const image = document.createElement("img");
                image.src = "/web/imgScript/" + product.image;
                image.alt = product.name;

                const name = document.createElement("p");
                name.textContent = product.name;

                const submitButton = document.createElement("button");
                submitButton.classList.add("submit-button");
                submitButton.textContent = "Add new offer";
                submitButton.addEventListener("click", function (event) {
                  event.preventDefault();
                  popupWindow.style.display = "block";
                  prodExists = false;
                  if (products.includes(product.name)) {
                    prodExists = true;
                    var values = {
                      spid: superId,
                      pname: product.name,
                    };
                    fetch("fetchOfferPrice.php", {
                      method: "POST",
                      headers: {
                        "Content-Type": "application/json",
                      },
                      body: JSON.stringify(values),
                    })
                      .then((response) => response.text())
                      .then((result) => {
                        oldPrice = result;
                      });
                  }
                  prodName = product.name;
                  console.log(products);
                });

                const productInfo = document.createElement("div");
                productInfo.classList.add("product-info");

                productItem.appendChild(image);
                productItem.appendChild(name);
                productItem.appendChild(submitButton);
                productGrid.appendChild(productItem);
              });
            } else {
              console.error("Error fetching data:", xhrProduct.statusText);
            }
          }
        };
        xhrProduct.send();
      });
    }
  };
  xhr.send();
});
