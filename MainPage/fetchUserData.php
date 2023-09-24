<?php
session_start();

if (isset($_SESSION['username'])) {
    $username = $_SESSION['username'];
    
    // Replace these values with your database connection details
    $conn = new mysqli('localhost', 'root', '', 'webdev');
    
    if ($conn->connect_error) {
        echo json_encode(array('status' => 'error', 'message' => 'Connection Failed: ' . $conn->connect_error));
        exit;
    } else {
        $sql = "SELECT current_tokens, current_score, total_score FROM user WHERE username='$username'";
        $result = mysqli_query($conn, $sql);

        if ($result) {
            $userData = mysqli_fetch_assoc($result);
            echo json_encode(array('status' => 'success', 'data' => $userData));
        } else {
            echo json_encode(array('status' => 'error', 'message' => 'Failed to fetch user data.'));
        }

        $conn->close();
    }
} else {
    echo json_encode(array('status' => 'error', 'message' => 'User not authenticated.'));
}
?>
