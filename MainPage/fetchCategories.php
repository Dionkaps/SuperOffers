<?php
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}

//Retrieve the categories name
$sql = 'SELECT name FROM categories';
$result = $conn->query($sql);

$categories = array();
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $categories[] = $row['name'];
    }
}

$conn->close();

//Return the data in JSON format
header('Content-Type: application/json');
echo json_encode($categories);
