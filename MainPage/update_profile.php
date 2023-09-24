<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $newUsername = $_POST['newUsername'];
    $newPassword = $_POST['newPassword'];

    // Database connection
    $conn = new mysqli('localhost', 'root', '', 'webdev');
    if ($conn->connect_error) {
        echo json_encode(array('status' => 'error', 'message' => 'Connection Failed: ' . $conn->connect_error));
        exit;
    } else {
        $username = $_SESSION['username'];
        $sql = "SELECT * FROM user WHERE username='$username'";
        $result = mysqli_query($conn, $sql);

        if (mysqli_num_rows($result) == 1) {
            $updateStmt = $conn->prepare("UPDATE user SET username = ?, password = ? WHERE username = ?");
            $updateStmt->bind_param("sss", $newUsername, $newPassword, $username);
            $updateResult = $updateStmt->execute();

            if ($updateResult) {
                $_SESSION['username'] = $newUsername;
                $_SESSION['password'] = $newPassword;
                echo json_encode(array('status' => 'success', 'message' => 'Username and password updated successfully.'));
            } else {
                echo json_encode(array('status' => 'error', 'message' => 'Failed to update username and password].'));
            }

            $updateStmt->close();
        } else {
            echo json_encode(array('status' => 'error', 'message' => 'User not found.'));
        }

        $conn->close();
    }
} else {
    echo json_encode(array('status' => 'error', 'message' => 'Invalid request.'));
}
?>
