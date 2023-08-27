<?php
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$query = $_GET["query"];
$query = mysqli_real_escape_string($conn, $query);

// Set UTF-8 encoding
$conn->set_charset("utf8mb4");

$sql = "SELECT DISTINCT name FROM products WHERE name LIKE '%$query%'";
$result = $conn->query($sql);

$autocompleteResults = array();
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $autocompleteResults[] = $row["name"];
    }
}

$conn->close();

header("Content-Type: application/json; charset=utf-8");
echo json_encode($autocompleteResults, JSON_UNESCAPED_UNICODE);
?>
