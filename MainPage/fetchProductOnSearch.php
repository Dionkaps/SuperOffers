<?php
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';


// Get the selected category from the query string
if (isset($_GET["searchedName"])) {
    $searchedName = $_GET["searchedName"];
} else {
    die("Searched name is missing.");
}


$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}
// Set UTF-8 encoding
$conn->set_charset("utf8mb4");

$productQuery = "SELECT DISTINCT id, name, image FROM products WHERE name LIKE '%$searchedName%'";
$resultProducts = $conn->query($productQuery);

$products = array();


    while ($product = $resultProducts->fetch_assoc()) {
        $products[] = $product;
    }

$conn->close();

header('Content-Type: application/json');
echo json_encode($products, JSON_UNESCAPED_UNICODE);
