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
    $uid = $data['userid'];  //User ID of the user that submitted the offer that is being rated

    $queryProdId = "SELECT id FROM products WHERE name = ?";
    $stmtProdId = $conn->prepare($queryProdId);
    $stmtProdId->bind_param("s", $pName);
    $stmtProdId->execute();
    $resultProdId = $stmtProdId->get_result();

    if ($resultProdId->num_rows > 0) {
        $row = $resultProdId->fetch_assoc();
        $prodId = $row['id'];

        // Construct the SQL query to update the "stock" column in the "discount" table
        $sqlUpdate = "UPDATE discount SET stock = 0 WHERE user_id = ? AND shop_id = ? AND product_id = ? AND active = 1";
        $stmtUpdate = $conn->prepare($sqlUpdate);
        $stmtUpdate->bind_param("iss", $uid, $spId, $prodId);
        if ($stmtUpdate->execute()) {
            echo "Stock updated successfully!";
        } else {
            echo "Error updating stock: " . $conn->error;
        }
    } else {
        echo "Error executing the second query: " . $conn->error;
    }
    $conn->close();
}
