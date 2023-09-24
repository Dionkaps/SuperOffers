<?php
if (count($argv) < 2) {
    echo "Usage: php splitTokens.php <totalTokens>";
    exit(1);
}
$totalTokens = $argv[1];

$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';

// Create a connection to the database
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Start a transaction
$conn->begin_transaction();

// SQL query to calculate the sum of current_score
$sql = "SELECT SUM(current_score) AS total_score FROM user";

$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Fetch the result
    $row = $result->fetch_assoc();
    $totalScore = $row['total_score'];
    if ($totalScore == 0) {
        echo "Total score is 0. No tokens to split.";
    } else {
        // Calculate tokensPerScore
        $tokensPerScore = $totalTokens / $totalScore;

        // Update each user's current_score based on tokensPerScore and update total_score
        $updateSql = "UPDATE user SET current_score = ROUND(current_score * $tokensPerScore), total_score = total_score + ROUND(current_score * $tokensPerScore), current_tokens = 0, current_score = 0";

        if ($conn->query($updateSql) === TRUE) {
            echo "User scores and total_score updated successfully!";
            // Commit the transaction
            $conn->commit();
        } else {
            echo "Error updating user scores: " . $conn->error;
            // Rollback the transaction in case of an error
            $conn->rollback();
        }
    }
} else {
    echo "No records found in the 'user' table.";
    // Rollback the transaction if no records are found
    $conn->rollback();
}

// Close the database connection
$conn->close();
