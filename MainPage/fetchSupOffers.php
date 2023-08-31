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
    $supName = $data['spname'];
    $catName = $data['catname'];

    //Shop ID
    $queryShopName = "SELECT shop_id FROM shop WHERE name = '" . $supName . "'";
    $resultShopId = $conn->query($queryShopName);

    if ($resultShopId) {
        $row = $resultShopId->fetch_assoc();
        $shopId = $row['shop_id'];
    }

    //Category ID
    $queryCatName = "SELECT id FROM categories WHERE name = '" . $catName . "'";
    $resultCatId = $conn->query($queryCatName);

    if ($resultCatId) {
        $row = $resultCatId->fetch_assoc();
        $catId = $row['id'];
    }


    $query = "SELECT product_id FROM discount WHERE shop_id = ?";

    $stmt = $conn->prepare($query);
    $stmt->bind_param("s", $shopId);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result) {
        while ($row = $result->fetch_assoc()) {
            $productId = $row['product_id'];

            $stmt1 = $conn->prepare("SELECT name FROM products WHERE id = ? AND category_id = ?");
            $stmt1->bind_param("ss", $productId, $catId);

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
