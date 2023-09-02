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
    $prodName = $data['pname'];

    $queryProducts = "SELECT id FROM products WHERE name = '" . $prodName . "'";
    $resultPordId = $conn->query($queryProducts);

    if ($resultPordId) {
        $row = $resultPordId->fetch_assoc();
        $productId = $row['id'];
    }

    $query = "SELECT discount_price, likes, dislikes, date FROM discount
          WHERE product_id = ? AND shop_id = ?";

    $stmt = $conn->prepare($query);
    $stmt->bind_param("ss", $productId, $spId);
    $stmt->execute();
    $result = $stmt->get_result();
    $response = array();
    while ($row = $result->fetch_assoc()) {
        $item = array(
            "discount_price" => $row['discount_price'],
            "likes" => $row['likes'],
            "dislikes" => $row['dislikes'],
            "date" => $row['date']
        );
        $response[] = $item;
    }

    echo json_encode($response);
}