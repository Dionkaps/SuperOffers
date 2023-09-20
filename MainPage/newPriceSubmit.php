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
$active = 1;
session_start();
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $email = $_SESSION['email'];

    $query1 = "SELECT user_id FROM user WHERE email = ?";

    $stmt1 = $conn->prepare($query1);
    $stmt1->bind_param("s", $email);
    $stmt1->execute();
    $result1 = $stmt1->get_result();

    if ($result1) {
        while ($row = $result1->fetch_assoc()) {
            $userId = $row['user_id'];
        }
    } else {
        echo "Error executing the first query: " . $conn->error;
    }

    $query = "SELECT id FROM products WHERE name = ?";

    $stmt = $conn->prepare($query);
    $stmt->bind_param("s", $prodName);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result) {
        while ($row = $result->fetch_assoc()) {
            $productId = $row['id'];
        }
        $insertPriceQuery = "INSERT INTO discount (product_id, discount_price, shop_id, likes, dislikes, stock, date, user_id, active) VALUES 
        ( $productId, $newOfferPrrice, '$superId', $likes, $dislikes, $stock, '$currentDate', $userId, $active)";
        mysqli_query($conn, $insertPriceQuery);
        header('Location:../MainPage/main_page.html');
    } else {
        echo "Error executing the first query: " . $conn->error;
    }
}
