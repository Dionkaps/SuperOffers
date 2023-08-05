<?php
$host = "localhost";
$username = "root";
$password = "";
$dbname = "webdev";
$conn = new mysqli($host, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

//Decode the GeoJSON data
$json_string = file_get_contents('map_data.geojson');
$map_data = json_decode($json_string, true);
$shop_data = $map_data['features'];

//Prepared statements
$stmt_shops = $conn->prepare("INSERT INTO shop (shop_id, name ) VALUES (?,?)");
$stmt_shops->bind_param("ss", $shop_id, $name);

//Get shop data from json and insert them in the database
foreach ($shop_data as $feature) {
    $shop_id = $feature['id'];
    $properties = $feature['properties'];
    $name = $properties['name'];

    if ($stmt_shops->execute()) {
        echo "Shops inserted successfully. <br>";
    } else {
        echo "Error inserting shop: " . $conn->error . "<br>";
    }
}


//Connections termination
$stmt_shops->close();

$conn->close();