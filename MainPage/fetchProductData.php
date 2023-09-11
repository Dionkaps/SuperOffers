<?php
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';


if (isset($_GET["subcategory"])) {
    $selectedSubcategoryId = $_GET["subcategory"];
} else {
    die("Subcategory parameter is missing.");
}

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}

$productQuery = "SELECT id, name, image FROM products WHERE subcategory_id = ?";

$stmt = $conn->prepare($productQuery);
$stmt->bind_param("s", $selectedSubcategoryId);
$stmt->execute();
$resultProducts = $stmt->get_result();

$products = array();

while ($product = $resultProducts->fetch_assoc()) {
    $products[] = $product;
}

$conn->close();

header('Content-Type: application/json');
echo json_encode($products, JSON_UNESCAPED_UNICODE);
?>