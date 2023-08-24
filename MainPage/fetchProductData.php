<?php
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';

// Get the selected category from the query string
if (isset($_GET["subcategory"])) {
    $selectedSubcategoryId = $_GET["subcategory"];
} else {
    die("Category parameter is missing.");
}

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}

$productQuery = "SELECT id, name, image FROM products WHERE subcategory_id = '" . $selectedSubcategoryId . "'";
$resultProducts = $conn->query($productQuery);

$products = array();


    while ($product = $resultProducts->fetch_assoc()) {
        $products[] = $product;
    }

$conn->close();

header('Content-Type: application/json');
echo json_encode($products, JSON_UNESCAPED_UNICODE);
?>