<?php

$conn = new mysqli("localhost", "root", "", "webdev");

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL query to delete related records from the "discount" table
$sql_discount = "DELETE FROM discount WHERE product_id IN (SELECT id FROM products)";

if ($conn->query($sql_discount) === TRUE) {
    echo "";
} else {
    echo "Error deleting discount records: " . $conn->error;
}

// SQL query to delete all data from products
$sql_products = "DELETE FROM products";
$sql_products = "DELETE FROM prices";

if ($conn->query($sql_products) === TRUE) {
    echo "All product , pricing data and related discounts deleted successfully.";
} else {
    echo "Error deleting data: " . $conn->error;
}

// Close the database connection
$conn->close();
?>
