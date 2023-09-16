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
    } else {
        echo "Product not found";
    }

    $sql = "DELETE FROM discount WHERE shop_id = ? AND product_id = ?";

    $stmt = $conn->prepare($sql);

    if ($stmt === FALSE) {
        die("Error preparing statement: " . $conn->error);
    }

    $stmt->bind_param("ss", $spId, $prodId);

    if ($stmt->execute() === TRUE) {
        echo "Record deleted successfully";
    } else {
        echo "Error deleting record: " . $stmt->error;
    }

    $stmt->close();
}
$conn->close();
