<?php
session_start();

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
    $_SESSION['spid'] = $spId;

    $query = "SELECT product_id FROM discount WHERE shop_id = ?";

    $stmt = $conn->prepare($query);
    $stmt->bind_param("s", $spId);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result) {
        while ($row = $result->fetch_assoc()) {
            $productId = $row['product_id'];

            $stmt1 = $conn->prepare("SELECT name FROM products WHERE id = ?");
            $stmt1->bind_param("s", $productId);

            $stmt1->execute();

            $result1 = $stmt1->get_result();
            $row1 = $result1->fetch_assoc();

            if ($row1) {
                $results = $row1['name'];
                echo $results . "~";
            }
        }
    } else {
        echo "Error executing the first query: " . $conn->error;
    }
    $stmt->close();
}
$conn->close();
