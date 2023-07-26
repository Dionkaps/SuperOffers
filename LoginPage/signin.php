<?php
$email = $_POST['email'];
$password = $_POST['password'];

// Database connection
$conn = new mysqli('localhost','root','','webdev');
if($conn->connect_error){
    echo "$conn->connect_error";
    die("Connection Failed : ". $conn->connect_error);
} else {
    $sql = "select * from user where email='$email'AND password='$password'";

    $result = mysqli_query($conn,$sql);

    if(mysqli_num_rows($result)==1){
        echo "Correct";
        exit();
    }
    else if(mysqli_num_rows($result)!=1){
        echo "Wrong";
    }
    
}
?>