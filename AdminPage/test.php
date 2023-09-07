<?php
// Replace with your actual database credentials
$hostname = "localhost";
$username = "root";
$password = "";
$database = "webdev";

// Create a connection to the database
$conn = new mysqli($hostname, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get the selected month and year from the URL query parameter
$monthYear = $_GET["monthYear"];

// SQL query to count entries for the selected month and year
$sql = "SELECT COUNT(*) AS entry_count FROM discount WHERE DATE_FORMAT(date, '%Y-%m') = '$monthYear'";

$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    echo $row["entry_count"];
} else {
    echo "0";
}

$conn->close();
?>
