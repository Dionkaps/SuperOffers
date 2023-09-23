<?php
$conn = new mysqli("localhost", "root", "", "webdev");

// Check if the connection was successful
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


$sql = "DELETE FROM shop";

if ($conn->query($sql) === TRUE) {
    echo "Shop data deleted successfully";
} else {
    echo "Error deleting data: " . $conn->error;
}

// Close the database connection
$conn->close();
?>

