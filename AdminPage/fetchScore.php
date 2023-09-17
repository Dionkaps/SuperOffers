<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "webdev";

// Create a connection to the database
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Fetch user data and sort by tokens
$sql = "SELECT username, total_score,token_count FROM user ORDER BY total_score DESC";
$result = $conn->query($sql);

// Create an array to store user data
$users = array();

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $users[] = $row;
    }
}

// Close the database connection
$conn->close();

// Return JSON-encoded user data
echo json_encode($users);
?>
