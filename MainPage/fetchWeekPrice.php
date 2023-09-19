<?php
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $jsonData = file_get_contents("php://input");
    $data = json_decode($jsonData, true);
    $pName = $data['pname'];

    $queryProdId = "SELECT id FROM products WHERE name = ?";
    $stmtProdId = $conn->prepare($queryProdId);
    $stmtProdId->bind_param("s", $pName);
    $stmtProdId->execute();
    $resultProdId = $stmtProdId->get_result();

    if ($resultProdId->num_rows > 0) {
        $row = $resultProdId->fetch_assoc();
        $prodId = $row['id'];

        // Calculate the date one week ago from the current date
        $oneWeekAgo = date('Y-m-d', strtotime('-1 week'));

        // Create variables for binding
        $productId = $prodId;
        $startDate = $oneWeekAgo;
        $endDate = date('Y-m-d');

        // Modify the query to calculate the average price for the past week
        $query = "SELECT AVG(price) AS average_price FROM prices WHERE product_id = ? AND date >= ? AND date <= ?";
        $stmt = $conn->prepare($query);

        // Bind the variables
        $stmt->bind_param("sss", $productId, $startDate, $endDate);

        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows > 0) {
            $row = $result->fetch_assoc();
            $averagePrice = $row["average_price"];
            echo $averagePrice;
        } else {
            echo "No records found for the past week";
        }
    } else {
        echo "Product not found";
    }

    $stmt->close();
    $stmtProdId->close();
}
$conn->close();
