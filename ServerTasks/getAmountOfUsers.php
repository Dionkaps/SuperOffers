<?php
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';

// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Execute a SQL query to count rows
$sql = "SELECT COUNT(*) AS total FROM user";

$result = $conn->query($sql);

if ($result) {
    $row = $result->fetch_assoc();
    $rowCount = $row['total'];
    echo $rowCount;
} else {
    echo "Error: " . $conn->error;
}

// Close the database connection
$conn->close();
