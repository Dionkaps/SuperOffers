<?php

$hostname = "localhost";
$username = "root";
$password = "";
$database = "webdev";

$conn = new mysqli($hostname, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get the selected month and year from the URL query parameter
$monthYear = $_GET["monthYear"];

// SQL query to count entries for each day of the selected month and year
$sql = "SELECT DATE(date) AS day, COUNT(*) AS entry_count FROM discount WHERE DATE_FORMAT(date, '%Y-%m') = '$monthYear' GROUP BY day";

$result = $conn->query($sql);

$data = array();

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $data[$row["day"]] = $row["entry_count"];
    }
}

header('Content-Type: application/json');
echo json_encode($data);

$conn->close();
?>
