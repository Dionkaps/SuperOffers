<?php
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';
$active = 1;
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $jsonData = file_get_contents("php://input");
    $data = json_decode($jsonData, true);
    $spId = $data['spid'];
    $prodName = $data['pname'];

    $queryProducts = "SELECT id FROM products WHERE name = ?";
    $stmt1 = $conn->prepare($queryProducts);
    $stmt1->bind_param("s", $prodName);
    $stmt1->execute();
    $resultPordId = $stmt1->get_result();

    if ($resultPordId) {
        $row = $resultPordId->fetch_assoc();
        $productId = $row['id'];
    }

    $query = "SELECT discount_price, likes, dislikes, date, stock, user_id FROM discount
          WHERE product_id = ? AND shop_id = ? AND active = ?";

    $stmt = $conn->prepare($query);
    $stmt->bind_param("ssi", $productId, $spId, $active);
    $stmt->execute();
    $result = $stmt->get_result();
    $response = array();
    while ($row = $result->fetch_assoc()) {
        $item = array(
            "discount_price" => $row['discount_price'],
            "likes" => $row['likes'],
            "dislikes" => $row['dislikes'],
            "date" => $row['date'],
            "stock" => $row['stock'],
            "user_id" => $row['user_id']

        );
        $response[] = $item;
    }
    $stmt->close();
    echo json_encode($response);
}
$conn->close();
