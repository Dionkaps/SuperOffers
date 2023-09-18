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
    $spId = $data['spid'];
    $pName = $data['pname'];

    $queryProdId = "SELECT id FROM products WHERE name = ?";
    $stmtProdId = $conn->prepare($queryProdId);
    $stmtProdId->bind_param("s", $pName);
    $stmtProdId->execute();
    $resultProdId = $stmtProdId->get_result();

    if ($resultProdId->num_rows > 0) {
        $row = $resultProdId->fetch_assoc();
        $prodId = $row['id'];

        $query = "SELECT discount_price FROM discount WHERE shop_id = ? AND product_id = ? AND active = 1";
        $stmt = $conn->prepare($query);
        $stmt->bind_param("ss", $spId, $prodId);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows > 0) {
            $row = $result->fetch_assoc();
            $currentValue = $row["discount_price"];
            echo $currentValue;
        } else {
            echo "No records found";
        }
    } else {
        echo "Product not found";
    }

    $stmt->close();
    $stmtProdId->close();
}
$conn->close();
