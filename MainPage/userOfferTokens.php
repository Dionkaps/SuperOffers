<?php
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';
session_start();
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $jsonData = file_get_contents("php://input");
    $data = json_decode($jsonData, true);
    $score = $data['score'];
    $email = $_SESSION['email'];

    // First, get the current_score
    $queryGetScore = "SELECT current_score FROM user WHERE email = ?";
    $stmtGetScore = $conn->prepare($queryGetScore);
    $stmtGetScore->bind_param("s", $email);
    $stmtGetScore->execute();
    $result = $stmtGetScore->get_result();

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $currentScore = $row['current_score'];

        // Update the current_score with its old value plus the new score
        $newScore = $currentScore + $score;

        $queryUpdateScore = "UPDATE user SET current_score = ? WHERE email = ?";
        $stmtUpdateScore = $conn->prepare($queryUpdateScore);
        $stmtUpdateScore->bind_param("is", $newScore, $email);

        if ($stmtUpdateScore->execute()) {
            echo "Value increased successfully";
        } else {
            echo "Error updating record: " . $stmtUpdateScore->error;
        }

        $stmtUpdateScore->close();
    } else {
        echo "User not found";
    }

    $stmtGetScore->close();
}
$conn->close();
