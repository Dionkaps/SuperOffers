document.addEventListener("DOMContentLoaded", function () {
    const categoryDropdown = document.getElementById("categories");
    const subcategoryDropdown = document.getElementById("subcategories");
    const searchBox = document.getElementById("searchBox");
    const productGrid = document.querySelector('.product-grid');

    //Searchbar

    searchBox.addEventListener("input", function () {
        const inputValue = searchBox.value.trim();

        if (inputValue.length >= 2) {
            fetch("fetchProductOnSearch.php?searchedName=" + inputValue)
                .then(response => response.json())
                .then(data => {
                    productGrid.innerHTML = ''; // Clear existing content

                    data.forEach(product => {
                        const productItem = document.createElement('div');
                        productItem.classList.add('product-item');

                        const image = document.createElement('img');
                        image.src = "/web/imgScript/" + product.image;
                        image.alt = product.name;

                        const name = document.createElement('p');
                        name.textContent = product.name;

                        const submitButton = document.createElement('button');
                        submitButton.classList.add('submit-button');
                        submitButton.textContent = 'Submit offer';

                        const productInfo = document.createElement('div');
                        productInfo.classList.add('product-info');

                        productItem.appendChild(image);
                        productItem.appendChild(name);
                        productItem.appendChild(submitButton);
                        productGrid.appendChild(productItem);
                    });
                });
        } else {
            productGrid.innerHTML = ''; // Clear existing content
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

                                const submitButton = document.createElement('button');
                                submitButton.classList.add('submit-button');
                                submitButton.textContent = 'Submit offer';

                                const productInfo = document.createElement('div');
                                productInfo.classList.add('product-info');

                                productItem.appendChild(image);
                                productItem.appendChild(name);
                                productItem.appendChild(submitButton);
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
