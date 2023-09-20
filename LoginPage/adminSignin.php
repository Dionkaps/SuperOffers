<?php
session_start();

$username = $_POST['username'];
$password = $_POST['password'];

// Database connection
$conn = new mysqli('localhost', 'root', '', 'webdev');
if ($conn->connect_error) {
    echo "$conn->connect_error";
    die("Connection Failed : " . $conn->connect_error);
} else {
    $sql = "SELECT * FROM admin WHERE username='$username' AND password='$password'";

    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) == 1) {
        $user_data = mysqli_fetch_assoc($result);
        
        // Store user data in session
        $_SESSION['username']=$user_data['username'];
        $_SESSION['password']=$user_data['password'];
    
        
        echo "Correct";
        exit();
    } else {
        echo "Wrong";
    }
}

$conn->close();
?>
