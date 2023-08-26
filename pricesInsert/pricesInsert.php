<?php
$host = "localhost";
$username = "root";
$password = "";
$dbname = "webdev";
$conn = new mysqli($host, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$json = file_get_contents('prices.json');

$data = json_decode($json, true);

foreach ($data['data'] as $product) {
    $productId = $product['id'];

    $productPrices = $product['prices'];

    //Insert prices into the prices table
    foreach ($productPrices as $price) {
        $date = $price['date'];
        $priceValue = $price['price'];

        $insertPriceQuery = "INSERT INTO prices (product_id, date, price) VALUES ( $productId, '$date', $priceValue)";
        mysqli_query($conn, $insertPriceQuery);
    }
}


$conn->close();
