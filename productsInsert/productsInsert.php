<?php
$host = "localhost";
$username = "root";
$password = "";
$dbname = "webdev";
$conn = new mysqli($host, $username, $password, $dbname);
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

//Decode the JSON data
$json_string = file_get_contents('products_data.json');
$data = json_decode($json_string, true);

//Prepared statements
$stmt_products = $conn->prepare("INSERT INTO products (id, name, category_id, subcategory_id) VALUES (?, ?, ?, ?)");
$stmt_products->bind_param("ssss", $id, $name, $category_id, $subcategory_id);

$stmt_categories = $conn->prepare("INSERT INTO categories (id, name) VALUES (?, ?)");
$stmt_categories->bind_param("ss", $category_id, $category_name);

$stmt_subcategories = $conn->prepare("INSERT INTO subcategories (id, name, category_id) VALUES (?, ?, ?)");
$stmt_subcategories->bind_param("sss", $subcategory_uuid, $subcategory_name, $category_id);

//Get category data from json and insert them in database
foreach ($data['categories'] as $category) {
  $category_id = $category['id'];
  $category_name = $category['name'];

  if ($stmt_categories->execute()) {
    echo "Category inserted successfully. <br>";
  } else {
    echo "Error inserting category: " . $conn->error . "<br>";
  }

  //Get subcategory data from json and insert them in database
  foreach ($category['subcategories'] as $subcategory) {
    $subcategory_name = $subcategory['name'];
    $subcategory_uuid = $subcategory['uuid'];

    if ($stmt_subcategories->execute()) {
      echo "Subcategory inserted successfully. <br>";
    } else {
      echo "Error inserting subcategory: " . $conn->error . "<br>";
    }
  }
}

//Get product data from json and insert them in database
foreach ($data['products'] as $product) {
  $id = $product['id'];
  $name = $product['name'];
  $category_id = $product['category'];
  $subcategory_id = $product['subcategory'];

  if ($stmt_products->execute()) {
    echo "Product inserted successfully. <br>";
  } else {
    echo "Error inserting product: " . $conn->error . "<br>";
  }
}

//Connections termination
$stmt_products->close();
$stmt_categories->close();
$stmt_subcategories->close();

$conn->close();
