<?php
session_start();

$email = $_POST['email'];
$password = $_POST['password'];

// Database connection
$conn = new mysqli('localhost', 'root', '', 'webdev');
if ($conn->connect_error) {
    echo "$conn->connect_error";
    die("Connection Failed : " . $conn->connect_error);
} else {
    $sql = "SELECT * FROM user WHERE email='$email' AND password='$password'";

    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) == 1) {
        $user_data = mysqli_fetch_assoc($result);
        
        // Store user data in session
        $_SESSION['username']=$user_data['username'];
        $_SESSION['email'] = $user_data['email']; // Replace 'id' with your actual user ID column name
        $_SESSION['password']=$user_data['password'];
    
        
        echo "Correct";
        exit();
    } else {
        echo "Wrong";
    }
}

$conn->close();
?>
