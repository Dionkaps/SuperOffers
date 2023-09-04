document.addEventListener("DOMContentLoaded", function () {
  const shopDetails = document.getElementById("shop-name");

  function populateShopInfo(shopName){
    const shopName = document.createElement('p');
  }

  //Offer infobox populate function
  function offerPopulate() {
    infobox_body.innerHTML = ""; //Clear existing content
    //Offer search for chosen supermarket and category
    if (superId != null) {
      var values = {
        spid: superId
      }
      fetch("fetchSupOffers.php", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(values)
      })
        .then(response => response.text())
        .then(result => {
          const items = result.split("~");


          //Create a container for the items
          const itemsContainer = document.createElement("div");

          items.forEach(item => {
            if (item.trim() != "") {
              const itemElement = document.createElement("p");
              itemElement.textContent = item.trim();
              itemElement.style.fontWeight = "bold";
              itemElement.id = "itemElement";
              const likeButton = document.createElement("button");
              likeButton.textContent = "Like";
              likeButton.style.backgroundColor = "#69db69";
              likeButton.style.color = "black";
              likeButton.style.borderRadius = "5px";
              likeButton.addEventListener("click", () => {
                var values = {
                  spid: superId,
                  pname: item.trim()
                }
                fetch("likeOffer.php", {
                  method: "POST",
                  headers: {
                    "Content-Type": "application/json"
                  },
                  body: JSON.stringify(values)
                })
                  .then(response => response.text())
                  .then(result => {
                    if (result === "Value increased successfully") {
                      alert("Succsessfully liked offer");
                    }
                  });
              });


              const dislikeButton = document.createElement("button");
              dislikeButton.textContent = "Dislike";
              dislikeButton.style.backgroundColor = "#ff7a7a";
              dislikeButton.style.color = "black";
              dislikeButton.style.borderRadius = "5px";
              dislikeButton.addEventListener("click", () => {
                var values = {
                  spid: superId,
                  pname: item.trim()
                }
                fetch("dislikeOffer.php", {
                  method: "POST",
                  headers: {
                    "Content-Type": "application/json"
                  },
                  body: JSON.stringify(values)
                })
                  .then(response => response.text())
                  .then(result => {
                    if (result === "Value increased successfully") {
                      alert("Succsessfully disliked offer");
                    }
                  });
              });

              const buttonContainer = document.createElement("div");
              buttonContainer.appendChild(likeButton);
              buttonContainer.appendChild(dislikeButton);

              const itemContainer = document.createElement("div");
              itemContainer.classList.add("item-container");

              const firstRow = document.createElement("div");
              firstRow.classList.add("item-row");
              const secondRow = document.createElement("div");
              secondRow.classList.add("item-row");
              firstRow.appendChild(itemElement);
              //firstRow.appendChild(buttonContainer);

              infobox_body.appendChild(itemContainer);

              var values = {
                spid: superId,
                pname: item.trim()
              }
              const priceNrating = document.createElement("p");
              const date = document.createElement("p");
              const br = document.createElement("br");

              fetch("fetchProductDataOfferRating.php", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json"
                },
                body: JSON.stringify(values)
              })
                .then(response => response.text())
                .then(result => {
                  const jsonResponse = JSON.parse(result);

                  // Create formatted text with italic styles
                  const formattedText = `<em>
                ${jsonResponse[0].discount_price}&nbsp;<i class="fa-solid fa-euro-sign euro"></i>&nbsp;
                ${jsonResponse[0].likes}&nbsp;<i class="fa-solid fa-thumbs-up like"></i>&nbsp;
                ${jsonResponse[0].dislikes}&nbsp;<i class="fa-solid fa-thumbs-down dislike"></i>&nbsp;</em>
              `;

                  priceNrating.innerHTML = formattedText;

                  const formattedDate = `&nbsp;&nbsp;<strong>Offer date:</strong> <em>${jsonResponse[0].date}</em>`;

                  date.innerHTML = formattedDate;
                });

              secondRow.appendChild(priceNrating);
              secondRow.appendChild(br);
              secondRow.appendChild(date);
              itemContainer.appendChild(firstRow);
              itemContainer.appendChild(secondRow);
            }
          });
          if (result === "") {
            const itemElement = document.createElement("p");
            itemElement.textContent = "No offers found";
            infobox_body.appendChild(itemElement);
          }
          infobox_body.appendChild(itemsContainer);
        });

      console.log("Supermarket is inside the circle.");
      offerButtonInit();

      rateButtonInit();
      buttonsContainer.appendChild(offerbtn);
      buttonsContainer.appendChild(ratebtn);
      infobox_body.appendChild(buttonsContainer);
    }
  }

});