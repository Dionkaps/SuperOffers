<?php
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}

$queryCategories = "SELECT id, name FROM categories";
$stmtCategories = $conn->prepare($queryCategories);
$stmtCategories->execute();
$resultCategories = $stmtCategories->get_result();

$data = array();

while ($cat = $resultCategories->fetch_assoc()) {
    $selecteCategoryId = $cat['id'];
    $categories = array(
        "id" => $cat['id'],
        "name" => $cat['name'],
        "subcategories" => array()
    );

    $querySubcategories = "SELECT id, name FROM subcategories WHERE category_id = ?";
    $stmtSubcategories = $conn->prepare($querySubcategories);
    $stmtSubcategories->bind_param("i", $selecteCategoryId);
    $stmtSubcategories->execute();
    $resultSubcategories = $stmtSubcategories->get_result();

    while ($subcat = $resultSubcategories->fetch_assoc()) {
        $subcategories = array(
            "id" => $subcat['id'],
            "name" => $subcat['name']
        );
        array_push($categories['subcategories'], $subcategories);
    }

    array_push($data, $categories);
}

$jsonFile = array("categories" => $data);

$stmtCategories->close();
$stmtSubcategories->close();

$conn->close();

echo json_encode($jsonFile, JSON_UNESCAPED_UNICODE);
?>