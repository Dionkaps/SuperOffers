<?php
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}

// Fetch categories and subcategories from the database
$queryCategories = "SELECT id, name FROM categories"; // Adjust query as needed
$resultCategories = $conn->query($queryCategories);
$data = array();
while ($cat = $resultCategories->fetch_assoc()) {
    $selecteCategoryId = $cat['id'];
    $categories = array(        
            "id"=>$cat['id'],
            "name"=>$cat['name'],
            "subcategories"=>array()
    );
    $querySubcategories = "SELECT id, name FROM subcategories WHERE category_id ='" . $cat['id'] . "' "; // Adjust query as needed
    $resultSubcategories = $conn->query($querySubcategories);
    while ($subcat = $resultSubcategories->fetch_assoc()) {
        $subcategories = array(
            "id"=>$subcat['id'],
            "name"=>$subcat['name']
        );
        array_push($categories['subcategories'],$subcategories); 
    }
    array_push($data,$categories);
}

$jsonFile = array("categories"=>$data);


// Close the database connection
$conn->close();

// Set the response headers
echo json_encode($jsonFile, JSON_UNESCAPED_UNICODE);
?>
