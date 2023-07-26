<?php 
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
$conn = new mysqli('localhost','root','','webdev');
if($conn->connect_error){
    echo "$conn->connect_error";
    die("Connection Failed : ". $conn->connect_error);
} else {
    $sql = "select * from user where email='$email'";

    $result = mysqli_query($conn,$sql);

    if(mysqli_num_rows($result)==1){?> 
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8"/>
            <title></title>
        </head>
        <body>
            <script>
            window.location.assign('index.html');
            alert('User already exists');
            
            </script>
        </body>
    </html> 
    <?php
        exit();
    }

    else{
        $stmt = $conn->prepare("insert into user(username, password, email, token_count, like_count, dislike_count, total_score, current_score, first_name, last_name) values(?, ?, ?, ?, ?, ?, ?, ?, ? ,?)");
        $stmt->bind_param("sssiiiiiss", $username, $password, $email, $token_count, $like_count, $dislike_count, $total_score, $current_score, $firstName, $lastName);
        $execval = $stmt->execute(); 
        header('Location:/MainPage/main_page.html');
    }
    $stmt->close();
    $conn->close();
}
?>