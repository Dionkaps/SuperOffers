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
    $stmt1 = $conn->prepare($queryProducts);
    $stmt1->bind_param("s", $pName);
    $stmt1->execute();
    $resultPordId = $stmt1->get_result();

    if ($resultProdId) {
        $row = $resultProdId->fetch_assoc();
        $prodId = $row['id'];
    }

    $query = "SELECT dislikes FROM discount WHERE shop_id = ? AND product_id = ?";

    $stmt = $conn->prepare($query);
    $stmt->bind_param("ss", $spId, $prodId);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $currentValue = $row["dislikes"];

        $newValue = $currentValue + 1;

        $sqlUpdate = "UPDATE discount SET dislikes = ? WHERE shop_id = ? AND product_id = ?";

        $stmt = $conn->prepare($sqlUpdate);
        $stmt->bind_param("iss", $newValue, $spId, $prodId);

        if ($stmt->execute()) {
            echo "Value increased successfully";
        } else {
            echo "Error updating record: " . $stmt->error;
        }
    } else {
        echo "No records found";
    }

    $stmt->close();
}
