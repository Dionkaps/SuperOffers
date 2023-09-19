var userId;
document.addEventListener("DOMContentLoaded", function () {
  // const shopDetails = document.getElementById("shop-name");
  const offerGrid = document.querySelector(".offer-grid");

  /*
  function populateShopInfo(shopName){
    const shopDetails = document.createElement('p');
    shopDetails.textContent = 
  }
  */
  function offerPopulate() {
    offerGrid.innerHTML = ""; //Clear existing content

    fetch("../MainPage/getSupId.php", {
      method: "POST",
      headers: {
        "Content-Type": "text/plain",
      },
    })
      .then((response) => response.text())
      .then((result) => {
        superId = result.trim();
        console.log("Supermarket id is: " + superId);

        //Offer search for chosen supermarket and category
        if (superId != null) {
          console.log(superId);
          var values = {
            spid: superId,
          };
          fetch("../MainPage/fetchProductDataOfferRating.php", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(values),
          })
            .then((response) => response.text())
            .then((result) => {
              const items = JSON.parse(result);

              items.forEach((item) => {
                if (item.name.trim() != "") {
                  const offerContainer = document.createElement("div");
                  offerContainer.classList.add("offer-item");

                  const productImage = document.createElement("img");
                  productImage.src = "/web/imgScript/" + item.image;
                  productImage.alt = item.name.trim();

                  const itemElement = document.createElement("p");
                  itemElement.textContent = item.name.trim();
                  itemElement.style.fontWeight = "bold";
                  itemElement.id = "itemElement";
                 

                  const deleteButton = document.createElement("button");
                  deleteButton.textContent = "Delete";
                  deleteButton.style.backgroundColor = "#ff7a7a";
                  deleteButton.style.color = "black";
                  deleteButton.style.borderRadius = "5px";
                  deleteButton.addEventListener("click", () => {
                    var values = {
                      spid: superId,
                      pname: item.name.trim(),
                      userid: userId,
                    };
                    fetch("deleteOffer.php", {
                      method: "POST",
                      headers: {
                        "Content-Type": "application/json",
                      },
                      body: JSON.stringify(values),
                    })
                      .then((response) => response.text())
                      .then((result) => {
                        if (result === "Deletion completed successfully") {
                          alert("Deletion completed successfully");
                          window.history.back();

                        }
                      });
                  });

                  //Image container init
                  const imageContainer = document.createElement("div");

                  //Item container init
                  const itemContainer = document.createElement("div");
                  itemContainer.classList.add("item-container");

                  //Button container init
                  const buttonContainer = document.createElement("div");
                  buttonContainer.classList.add("button-container");

                  const firstRow = document.createElement("div");
                  firstRow.classList.add("product-details");
                  const secondRow = document.createElement("div");
                  secondRow.classList.add("offer-details");
                  const thirdRow = document.createElement("div");
                  thirdRow.classList.add("user-offer-details");

                  firstRow.appendChild(itemElement);

                  offerContainer.appendChild(itemContainer);

                  var values = {
                    spid: superId,
                    pname: item.name.trim(),
                  };
                  const priceNrating = document.createElement("p");
                  const date = document.createElement("p");
                  const userOfferDetails = document.createElement("p");
                  const br = document.createElement("br");

                  fetch("../MainPage/offerDetails.php", {
                    method: "POST",
                    headers: {
                      "Content-Type": "application/json",
                    },
                    body: JSON.stringify(values),
                  })
                    .then((response) => response.text())
                    .then((result) => {
                      const jsonResponse = JSON.parse(result);

                      // Create formatted text with italic styles
                      const formattedText = `<em>
                    ${jsonResponse[0].discount_price}&nbsp;<i class="fa-solid fa-euro-sign euro"></i>&nbsp;
                    ${jsonResponse[0].likes}&nbsp;<i class="fa-solid fa-thumbs-up like"></i>&nbsp;
                    ${jsonResponse[0].dislikes}&nbsp;<i class="fa-solid fa-thumbs-down dislike"></i>&nbsp;</em>
                    `;

                      priceNrating.innerHTML = formattedText;

                      var onStockResponse;
                      if (jsonResponse[0].stock == 1) {
                        onStockResponse = "On stock";
                        deleteButton.disabled = false;
                        deleteButton.style.backgroundColor =
                          "rgb(225, 75, 75)";
                      } else {
                        onStockResponse = "Out of stock";
                        deleteButton.disabled = true;
                        deleteButton.style.backgroundColor =
                          "rgb(237, 207, 207)";
                      }

                      const formattedDate = `<em>&nbsp;&nbsp;<strong>Offer date:</strong>${jsonResponse[0].date}&nbsp;<br>${onStockResponse}</em>`;

                      date.innerHTML = formattedDate;
                      userId = jsonResponse[0].user_id;
                      //User offer details

                      console.log("User id is: " + userId);
                      var values1 = {
                        uid: userId,
                      };

                      fetch("../MainPage/getUserDetails.php", {
                        method: "POST",
                        headers: {
                          "Content-Type": "application/json",
                        },
                        body: JSON.stringify(values1),
                      })
                        .then((response) => response.text())
                        .then((result) => {
                          console.log(result);
                          const jsonResponse = JSON.parse(result);
                          // Create formatted text with italic styles
                          const formattedText1 = `<em style="color: grey;">
                          Uploaded by:&nbsp;
                          ${jsonResponse[0].username}&nbsp;&nbsp;
                          Total score:&nbsp;
                          ${jsonResponse[0].total_score}&nbsp;</em>`;

                          userOfferDetails.innerHTML = formattedText1;
                        });
                    });

                  secondRow.appendChild(priceNrating);
                  secondRow.appendChild(br);
                  secondRow.appendChild(date);
                  console.log(userOfferDetails);
                  thirdRow.appendChild(userOfferDetails);
                  itemContainer.appendChild(firstRow);
                  itemContainer.appendChild(secondRow);
                  itemContainer.appendChild(thirdRow);

                  imageContainer.appendChild(productImage);

                  buttonContainer.appendChild(deleteButton);

                  offerContainer.appendChild(imageContainer);
                  offerContainer.appendChild(itemContainer);
                  offerContainer.appendChild(buttonContainer);
                  offerGrid.appendChild(offerContainer);
                }
              });
              if (result === "") {
                const itemElement = document.createElement("p");
                itemElement.textContent = "No offers found";
                offerContainer.appendChild(itemElement);
              }
            });

          console.log("Supermarket is inside the circle.");
        }
      });
  }
  offerPopulate();
});
