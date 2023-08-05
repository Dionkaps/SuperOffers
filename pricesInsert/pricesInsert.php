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
    $productName = $product['name'];
    $productPrices = $product['prices'];

    //Escape the product name to avoid SQL syntax errors
    $productName = mysqli_real_escape_string($conn, $productName);

    //Retrieve the product ID from the products table
    $productIdQuery = "SELECT id FROM products WHERE name = '$productName'";
    $result = mysqli_query($conn, $productIdQuery);

    //Check if the product exists in the products table
    if (mysqli_num_rows($result) > 0) {
        //Product exists, fetch the product ID
        $row = mysqli_fetch_assoc($result);
        $productId = $row['id'];

        //Insert prices into the prices table
        foreach ($productPrices as $price) {
            $date = $price['date'];
            $priceValue = $price['price'];

            $insertPriceQuery = "INSERT INTO prices (product_id, date, price) VALUES ( $productId, '$date', $priceValue)";
            mysqli_query($conn, $insertPriceQuery);
        }
    } else {
        //Handle the case where the product does not exist in the products table
        echo "Product '$productName' does not exist in the 'products' table. Skipping prices insertion.<br>";
    }
}

$conn->close();
