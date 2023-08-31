function fetchJSON(url) {
  return fetch(url).then(function (response) {
    return response.json();
  });
}
var data = fetchJSON("map_data.geojson").then(function (data) {
  //Sinartisi gia lipsi topothesias xristi
  function getUsersLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function (position) {
        //Apothikeusi sintetagmenwn
        var userLocation = new L.LatLng(
          position.coords.latitude,
          position.coords.longitude
        );

        //Estiasi sti topothesia xristi
        mymap.setView(userLocation, 16);
        var location_icon = L.icon({
          iconUrl: "images/giphy.gif",
          iconSize: [52, 68],
          iconAnchor: [26, 58],
        });

        //Afairesi marker me click button gia na min kanoun stack
        if (circle) mymap.removeLayer(circle);
        if (location_marker) mymap.removeLayer(location_marker);

        //Custom marker sti topothesia tou xristi
        location_marker = L.marker(userLocation, { icon: location_icon });
        location_marker.addTo(mymap);

        //Kiklos 50 metrwn me kentro ti topothesia tou xristi
        circle = L.circle(userLocation, {
          radius: 500,
          color: "blue",
          fillOpacity: 0.1,
          opacity: 0.7,
        }).addTo(mymap);
      });
    }
  }

  getUsersLocation();

  let mymap = L.map("map", {
    zoomControl: false,
    zoom: 12,
    center: L.latLng([38.246242, 21.7350847]),
  }); //set center

  mymap.addLayer(
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png")
  ); //base layer

  ////////////populate map with GeoJSON feature layer

  const myIcon = L.icon({
    iconUrl: "images/marker.png",
    iconSize: [32, 32],
    iconAnchor: [16, 22],
  });

  var featuresLayer = new L.GeoJSON(data, {
    onEachFeature: function (feature, marker) {
      marker.bindPopup("<h4>" + feature.properties.name + "</h4>");
    },
    pointToLayer: function (feature, latlng) {
      return L.marker(latlng, { icon: myIcon });
    },
  });
  featuresLayer.addTo(mymap);

  //searcbar
  let controlSearch = new L.Control.Search({
    position: "topleft",
    layer: featuresLayer,
    propertyName: "name",
    initial: false,
    zoom: 19,
    marker: false,
    collapsed: false, //Emfanizei apo tin arxi olokliro to searchbar kai oxi mono to button
    textPlaceholder: "Search for a supermarket...",
  }).addTo(mymap);

  L.control
    .zoom({
      position: "topleft",
    })
    .addTo(mymap);

  //Dimiourgia kai leitourgikotita find my location button
  var circle = null;
  var location_marker = null;

  const infobox_body = document.querySelector(".infobox_body");

  //Offer infobox populate function
  function offerPopulate() {
    infobox_body.innerHTML = ""; //Clear existing content
    //Offer search for chosen supermarket and category
    var values = {
      spname: s_name.innerHTML,
      catname: catName
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

            const likeButton = document.createElement("button");
            likeButton.textContent = "Like";
            likeButton.style.backgroundColor = "#69db69";
            likeButton.style.color = "black";
            likeButton.style.borderRadius = "5px";
            likeButton.addEventListener("click", () => {
              var values = {
                spname: s_name.innerHTML,
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
                spname: s_name.innerHTML,
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
            itemContainer.appendChild(itemElement);
            itemContainer.appendChild(buttonContainer);

            infobox_body.appendChild(itemContainer);
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
    let btn = document.createElement("button");
    btn.innerHTML = "Apply an offer";
    btn.id = "offerButton"; // Adding the id "offerButton"
    btn.onclick = function () {
      alert("Button is clicked");
    };
    infobox_body.appendChild(btn);

  }

  function infobox_populate(event) {
    //Dimiourgia leitourgias gia prosthiki prosforas
    //Elegxos iparksis tou circle sto map
    if (mymap.hasLayer(circle)) {
      //Sintetagmenes kentrou kiklou
      var circleCenter = circle.getLatLng();
      //Ipologismos apostasis marker apo kentro kiklou
      var distance = circleCenter.distanceTo(event.latlng);

      //Elegxos an to layer einai marker & an vrisketai entos tou kiklou
      if (event.layer instanceof L.Marker && distance <= circle.getRadius()) {
        if (catChosen == true) {
          offerPopulate();
        }
        else {
          console.log("No category chosen");
        }
      }

      else {
        console.log("Supermarket is outside the circle.");
        infobox_body.innerHTML = "Eisai makria apo ola ta supermarket";
      }
    } else {
      console.log("Circle has not been drawn yet");
    }
  }

  function infobox_attributes() {
    if (window.innerWidth > 1121) {
      element.classList.add("infobox");
      element.style.height = "400px";
      element.style.width = "370px";
      element.style.boxShadow = "5px 5px 10px 5px rgba(0, 0, 0, .4)";
    } else {
      element.style.height = "40%";
      element.style.width = "100%";
    }
  }

  //Lipsi onomatos supermarket apo to layer featuresLayer me click se marker
  const s_name = document.querySelector(".sm-name");
  var element = document.getElementById("infobox_id");
  var superChosen = false;

  featuresLayer.on("click", function (event) {
    superChosen = true;
    const supermarketName = event.layer.feature.properties.name;
    s_name.innerHTML = supermarketName;

    infobox_attributes();
    infobox_populate(event);
  });

  //Lipsi onomatos supermarket apo to layer controlSearch me epitixi anazitisi &
  //Topothetisi popup me to onoma tou sm sto location tou
  controlSearch.on("search:locationfound", function (event) {
    superChosen = true;
    const supermarketName = event.layer.feature.properties.name;
    s_name.innerHTML = supermarketName;
    event.layer.bindPopup(supermarketName).openPopup();

    infobox_attributes();
    infobox_populate(event);
  });

  //Anagnwrisi alagis mikous parathirou gia na allazei to infobox katallila
  window.addEventListener("resize", function () {
    if (window.innerWidth > 1121 && superChosen) {
      element.classList.add("infobox");
      element.style.height = "400px";
      element.style.width = "370px";
      element.style.boxShadow = "5px 5px 10px 5px rgba(0, 0, 0, .4)";
    } else if (window.innerWidth <= 1121 && superChosen) {
      element.style.height = "40%";
      element.style.width = "100%";
    }
  });

  //Populate the products categories sidebar
  var xhr = new XMLHttpRequest();
  var catChosen = false;
  var catName;
  xhr.open("GET", "fetchCategories.php", true);
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);

        var buttonContainer = document.getElementById("buttonContainer");
        buttonContainer.style.display = "flex";
        buttonContainer.style.flexDirection = "column";

        for (var i = 0; i < response.length; i++) {
          var category = response[i];

          var button = document.createElement("button");
          button.innerText = category;

          button.addEventListener("click", function () {
            catChosen = true;
            catName = this.innerText;
            data = { message: this.innerText };

            resetIcons(); //Reset all icons

            fetch("fetchOffers.php", {
              method: "POST",
              headers: {
                "Content-Type": "text/plain"
              },
              body: JSON.stringify(data)
            })
              .then(response => response.text())
              .then(result => {
                const items = result.split(",");
                items.forEach(item => {
                  changeIconOnOffer(item.trim()); //Icon update on offer found
                  console.log(item.trim());
                });
              });
            offerPopulate();
          });

          buttonContainer.appendChild(button);
        }
      } else {
        console.error("Error fetching data:", xhr.status);
      }
    }
  };
  xhr.send();

  //Custom offer icon
  const offerIcon = L.icon({
    iconUrl: "images/offer.png",
    iconSize: [32, 32],
    iconAnchor: [16, 22],
  });

  //Change supermarket icon if there is an offer there
  function changeIconOnOffer(nodeId) {

    featuresLayer.eachLayer(function (layer) {
      if (layer.feature.id === nodeId) {
        layer.setIcon(offerIcon);
      }
    });

  }

  //Reset all icons
  function resetIcons() {
    featuresLayer.eachLayer(function (layer) {
      layer.setIcon(myIcon);
    });
  }
});
