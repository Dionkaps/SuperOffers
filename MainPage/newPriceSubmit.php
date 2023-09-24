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
$flag = 1;
session_start();
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $oneWeekAgo = date('Y-m-d', strtotime('-1 week'));
    $startDate = $oneWeekAgo;
    $endDate = date('Y-m-d');
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

    // Fetch the most recent price for the product from the 'prices' table
    $query = "SELECT price FROM prices WHERE product_id = ? ORDER BY date DESC LIMIT 1";
    $stmt = $conn->prepare($query);
    $stmt->bind_param("s", $productId);
    $stmt->execute();
    $priceResult = $stmt->get_result();

    if ($priceResult->num_rows > 0) {
        $priceRow = $priceResult->fetch_assoc();
        $currentPrice = $priceRow["price"];

        // Check if the discount price is less than 80% of the current price
        if ($newOfferPrrice < 0.2 * $currentPrice) {
            $flag = 0;
        } else {
            //No offers
        }
    } else {
        echo "No records found for the most recent price.<br>";
        echo "<hr>"; // Separation line between records
    }

    $query1 = "SELECT AVG(price) AS average_price FROM prices WHERE product_id = ? AND date >= ? AND date <= ?";
    $stmt1 = $conn->prepare($query1);
    $stmt1->bind_param("sss", $productId, $startDate, $endDate);
    $stmt1->execute();
    $result1 = $stmt1->get_result();

    if ($result1->num_rows > 0) {
        $row = $result1->fetch_assoc();
        $averagePrice = $row["average_price"];
        if ($newOfferPrrice < 0.2 * $averagePrice) {
            $flag = 0;
        } else {
            //No offers
        }
    } else {
        echo "No records found for the past week";
    }

    if ($flag == 0) {
        // Delete the row from the 'discount' table
        $deleteQuery = "UPDATE discount SET special_offer = '1' WHERE product_id = ? AND shop_id = ?";
        $deleteStmt = $conn->prepare($deleteQuery);
        $deleteStmt->bind_param("ss", $productId, $superId);
        $deleteStmt->execute();
        $deleteStmt->close();
    }
}
