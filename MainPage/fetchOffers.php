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
    $data = json_decode($jsonData);
    $catName = $data->message;

    $queryCategories = "SELECT id FROM categories WHERE name = ?";
    $stmtCatId = $conn->prepare($queryCategories);
    $stmtCatId->bind_param("s", $catName);
    $stmtCatId->execute();
    $resultCatId = $stmtCatId->get_result();

    if ($resultCatId->num_rows > 0) {
        $row = $resultCatId->fetch_assoc();
        $categoryId = $row['id'];

        $query = "SELECT d.shop_id
                  FROM discount d
                  INNER JOIN products p ON d.product_id = p.id
                  WHERE p.category_id = ? AND d.active = 1";
        $stmt = $conn->prepare($query);
        $stmt->bind_param("s", $categoryId);
        $stmt->execute();
        $result = $stmt->get_result();

        while ($row = $result->fetch_assoc()) {
            $shopID = $row['shop_id'] . ',';
            echo $shopID;
        }

        $stmt->close();
    } else {
        echo "Category not found";
    }

    $stmtCatId->close();
}
$conn->close();
?>
