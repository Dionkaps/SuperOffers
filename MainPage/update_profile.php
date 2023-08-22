<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $newEmail = $_POST['newEmail'];
    $newPassword = $_POST['newPassword'];

    // Database connection
    $conn = new mysqli('localhost', 'root', '', 'webdev');
    if ($conn->connect_error) {
        echo "$conn->connect_error";
        die("Connection Failed : " . $conn->connect_error);
    } else {
        $username = $_SESSION['username'];
        $sql = "SELECT * FROM user WHERE username='$username'";
        $result = mysqli_query($conn, $sql);

        if (mysqli_num_rows($result) == 1) {
            $updateStmt = $conn->prepare("UPDATE user SET email = ?, password = ? WHERE username = ?");
            $updateStmt->bind_param("sss", $newEmail, $newPassword, $username);
            $updateResult = $updateStmt->execute();
            
            if ($updateResult) {
                $_SESSION['email'] = $newEmail;
                $_SESSION['password'] = $newPassword;
                $_SESSION['success_message'] = 'Email and username updated successfully.';
                header('Location: success_page.php');
                exit();
            } else {
                $_SESSION['error_message'] = 'Failed to update email and username.';
                header('Location: error_page.php');
                exit();
            }
            
            $updateStmt->close();
        } else {
            $_SESSION['error_message'] = 'User not found.';
            header('Location: error_page.php');
            exit();
        }

        $conn->close();
    }
} else {
    $_SESSION['error_message'] = 'Invalid request.';
    header('Location: error_page.php');
    exit();
}
?>
