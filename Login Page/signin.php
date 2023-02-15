<?php
$username = $_POST['username'];
$password = $_POST['password'];

// Database connection
$conn = new mysqli('localhost','root','','test');
if($conn->connect_error){
    echo "$conn->connect_error";
    die("Connection Failed : ". $conn->connect_error);
} else {
    $sql = "select * from registration where email='$username'AND password='$password'";

    $result = mysqli_query($conn,$sql);

    if(mysqli_num_rows($result)==1){
        echo "LOGGED IN";
        exit();
    }

    else{
        echo "NOT LOGGED IN";
    }
    $conn->close();
}