<?php
$newOfferPrrice = $_POST['newPrice'];
$superId = $_POST['superId'];
$prodName = $_POST['prodName'];
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';
$currentDate = date("Y-m-d H:i:s");
$likes = 0;
$dislikes = 0;
$stock = 1;
$userId = 1;
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $query = "SELECT id FROM products WHERE name = ?";

    $stmt = $conn->prepare($query);
    $stmt->bind_param("s", $prodName);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result) {
        while ($row = $result->fetch_assoc()) {
            $productId = $row['id'];
        }
        $insertPriceQuery = "INSERT INTO discount (product_id, discount_price, shop_id, likes, dislikes, stock, date, user_id) VALUES ( $productId, $newOfferPrrice, '$superId', $likes, $dislikes, $stock, '$currentDate', $userId)";
        mysqli_query($conn, $insertPriceQuery);
        header('Location:../MainPage/main_page.html');
    } else {
        echo "Error executing the first query: " . $conn->error;
    }
}
