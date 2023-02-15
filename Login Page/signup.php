<?php
$username = $_POST['username'];
$password = $_POST['password'];
$firstName = $_POST['firstName'];
$lastName = $_POST['lastName'];

// Database connection
$conn = new mysqli('localhost','root','','test');
if($conn->connect_error){
    echo "$conn->connect_error";
    die("Connection Failed : ". $conn->connect_error);
} else {
    $sql = "select * from registration where email='$username'";

    $result = mysqli_query($conn,$sql);

    if(mysqli_num_rows($result)==1){
        echo "USER ALREADY EXISTS";
        exit();
    }

    else{
        $stmt = $conn->prepare("insert into registration(first_name, last_name, email, password) values(?, ?, ?, ?)");
        $stmt->bind_param("ssss", $firstName, $lastName, $username, $password);
        $execval = $stmt->execute();
        echo "Ta vala";
    }
    $stmt->close();
    $conn->close();
}