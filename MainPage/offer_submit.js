document.addEventListener("DOMContentLoaded", function () {
    const categoryDropdown = document.getElementById("categories");
    const subcategoryDropdown = document.getElementById("subcategories");
    const searchBox = document.getElementById("searchBox");
    const searchResults = document.getElementById("searchResults");

    //Searchbar
    searchBox.addEventListener("input", function () {
        const inputValue = searchBox.value.trim();

        if (inputValue.length >= 2) {
            fetch("searchProduct.php?query=" + inputValue)
                .then(response => response.json())
                .then(data => {
                    searchResults.innerHTML = "";
                    data.forEach(item => {
                        const resultItem = document.createElement("p");
                        resultItem.textContent = item;
                        resultItem.classList.add("resultItem"); // Add class for styling
                        searchResults.appendChild(resultItem);

                        resultItem.addEventListener("click", function () {
                            searchBox.value = item;
                            searchResults.innerHTML = "";
                        });
                    });
                });
        } else {
            searchResults.innerHTML = "";
        }
    });

    // Function to populate dropdowns
    function populateDropdown(dropdown, data, dispText) {

        const first_option = document.createElement("option");
        first_option.textContent = dispText;

        dropdown.appendChild(first_option);
        data.forEach(item => {
            const option = document.createElement("option");
            option.value = item.id;
            option.textContent = item.name;
            dropdown.appendChild(option);
        });
    }

    //Options for display text(dispText)
    catDispText = 'Select a category';
    subcatDispText = 'Select a subcategory';

    // Fetch categories and subcategories using XMLHttpRequest
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "fetchCategoriesSubcategories.php", true); // Replace with the correct path to your JSON file
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const data = JSON.parse(xhr.responseText);
            populateDropdown(categoryDropdown, data.categories, catDispText);

            // Event listener for category dropdown change
            categoryDropdown.addEventListener("change", function () {
                const selectedCategoryId = categoryDropdown.value;
                const category = data.categories.find(category => category.id === selectedCategoryId);
                subcategoryDropdown.innerHTML = ""; // Clear existing options
                if (category) {
                    populateDropdown(subcategoryDropdown, category.subcategories, subcatDispText);
                }
            });
            subcategoryDropdown.addEventListener("change", function () {
                const selectedSubcategoryId = subcategoryDropdown.value;
                console.log(selectedSubcategoryId);

                //Fetch product data from selection
                const productGrid = document.querySelector('.product-grid');

                // Clear the existing content of the grid
                productGrid.innerHTML = '';

                const xhrProduct = new XMLHttpRequest();
                xhrProduct.open('GET', `fetchProductData.php?subcategory=${selectedSubcategoryId}`, true);
                xhrProduct.onreadystatechange = function () {
                    if (xhrProduct.readyState === XMLHttpRequest.DONE) {
                        if (xhrProduct.status === 200) {
                            const productData = JSON.parse(xhrProduct.responseText);
                            productData.forEach(product => {
                                const productItem = document.createElement('div');
                                productItem.classList.add('product-item');

                                const image = document.createElement('img');
                                image.src = "/web/imgScript/" + product.image;
                                image.alt = product.name;

                                const name = document.createElement('p');
                                name.textContent = product.name;

                                productItem.appendChild(image);
                                productItem.appendChild(name);

                                productGrid.appendChild(productItem);
                            });
                        } else {
                            console.error('Error fetching data:', xhrProduct.statusText);
                        }
                    }
                };
                xhrProduct.send();
            });
        }
    };
    xhr.send();
});

