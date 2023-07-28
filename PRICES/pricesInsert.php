<?php
$host = "localhost";
$username = "root";
$password = "";
$dbname = "webdev";
$conn = new mysqli($host, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$json = 'prices.json';

$data = json_decode($json, true);

//Insert prices into the 'prices' table
foreach ($data['data'] as $product) {
    //Get the product details from the JSON
    $productName = $product['name'];
    $productPrices = $product['prices'];

    //Retrieve the product ID from the 'products' table
    $productIdQuery = "SELECT id FROM products WHERE name = '$productName'";
    $result = mysqli_query($connection, $productIdQuery);

    //Check if the product exists in the 'products' table
    if (mysqli_num_rows($result) > 0) {
        //Product exists, fetch the product ID
        $row = mysqli_fetch_assoc($result);
        $productId = $row['id'];

        //Insert prices into the 'prices' table
        foreach ($productPrices as $price) {
            $date = $price['date'];
            $priceValue = $price['price'];

            //Insert price along with the corresponding product ID into the 'prices' table
            $insertPriceQuery = "INSERT INTO prices (product_id, date, price) VALUES ($productId, '$date', $priceValue)";
            mysqli_query($connection, $insertPriceQuery);
        }
    } else {
        //Handle the case where the product does not exist in the 'products' table
        //You can choose to skip inserting prices or handle it as per your requirements
        echo "Product '$productName' does not exist in the 'products' table. Skipping prices insertion.<br>";
    }
}
$conn->close();
