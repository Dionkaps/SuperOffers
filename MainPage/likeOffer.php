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
    $pName = $data['pname'];

    $queryShopId = "SELECT shop_id FROM shop WHERE name = '" . $supName . "'";
    $resultShopId = $conn->query($queryShopId);

    if ($resultShopId) {
        $row = $resultShopId->fetch_assoc();
        $shopId = $row['shop_id'];
    }

    $queryProdId = "SELECT id FROM products WHERE name = '" . $pName . "'";
    $resultProdId = $conn->query($queryProdId);

    if ($resultProdId) {
        $row = $resultProdId->fetch_assoc();
        $prodId = $row['id'];
    }

    $query = "SELECT likes FROM discount WHERE shop_id = ? AND product_id = ?";

    $stmt = $conn->prepare($query);
    $stmt->bind_param("ss", $shopId, $prodId);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $currentValue = $row["likes"];

        // Step 3: Increment the Value
        $newValue = $currentValue + 1;

        // Step 4: Update the Database
        $sqlUpdate = "UPDATE discount SET likes = $newValue WHERE shop_id = '" . $shopId . "' AND product_id = '" . $prodId . "'";
        if ($conn->query($sqlUpdate) === TRUE) {
            echo "Value increased successfully";
        } else {
            echo "Error updating record: " . $conn->error;
        }
    } else {
        echo "No records found";
    }

    $stmt->close();
}
