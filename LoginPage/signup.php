<?php
session_start();

$email = $_POST['email'];
$password = $_POST['password'];
$firstName = $_POST['firstName'];
$lastName = $_POST['lastName'];
$username = $_POST['username'];
$token_count = 0;
$like_count = 0;
$dislike_count = 0;
$total_score = 0;
$current_score = 0;

// Database connection
$conn = new mysqli('localhost', 'root', '', 'webdev');
if ($conn->connect_error) {
    echo "$conn->connect_error";
    die("Connection Failed : " . $conn->connect_error);
} else {
    $sql = "SELECT * FROM user WHERE email='$email'";

    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) == 1) {
        $_SESSION['error_message'] = 'User already exists';
        header('Location: error_page.php');
        exit();
    } else {
        $stmt = $conn->prepare("INSERT INTO user(username, password, email, token_count, like_count, dislike_count, total_score, current_score, first_name, last_name) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
        $stmt->bind_param("sssiiiiiss", $username, $password, $email, $token_count, $like_count, $dislike_count, $total_score, $current_score, $firstName, $lastName);
        $execval = $stmt->execute();
        $stmt->close();
        
        // Store user data in session
        $_SESSION['username'] = $username;
        $_SESSION['email'] = $email;
        
        header('Location:/MainPage/main_page.html');
    }

    $conn->close();
}
?>
