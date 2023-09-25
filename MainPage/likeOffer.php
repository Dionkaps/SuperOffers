<?php
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';
session_start();
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $jsonData = file_get_contents("php://input");
    $data = json_decode($jsonData, true);
    $spId = $data['spid'];
    $pName = $data['pname'];
    $uid = $data['userid']; //User ID of the user that submitted the offer that is being rated

    $current_email = $_SESSION['email'];
    $queryUserId = "SELECT user_id FROM user WHERE email = ?";
    $stmtUserId = $conn->prepare($queryUserId);
    $stmtUserId->bind_param("s", $current_email);
    $stmtUserId->execute();
    $result1 = $stmtUserId->get_result();

    if ($result1) {
        while ($row = $result1->fetch_assoc()) {
            $currentUserId = $row['user_id'];
        }
    } else {
        echo "Error executing the first query: " . $conn->error;
    }

    $currentDate = date("Y-m-d H:i:s"); //Fetch the current date
    $rating = 1; // When the user likes the offer the rating is 1

    $queryProdId = "SELECT id FROM products WHERE name = ?";
    $stmtProdId = $conn->prepare($queryProdId);
    $stmtProdId->bind_param("s", $pName);
    $stmtProdId->execute();
    $resultProdId = $stmtProdId->get_result();

    if ($resultProdId->num_rows > 0) {
        $row = $resultProdId->fetch_assoc();
        $prodId = $row['id'];

        $queryRating = "INSERT INTO rating (rating, product_id, user_id, shop_id, date) VALUES (?,?,?,?,?)";
        $stmtRating = $conn->prepare($queryRating);
        $stmtRating->bind_param("isiss", $rating, $prodId, $currentUserId, $spId, $currentDate);
        $stmtRating->execute();
        $stmtRating->close();

        $query = "SELECT likes FROM discount WHERE shop_id = ? AND product_id = ?";
        $stmt = $conn->prepare($query);
        $stmt->bind_param("ss", $spId, $prodId);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows > 0) {
            $row = $result->fetch_assoc();
            $currentValue = $row["likes"];

            $newValue = $currentValue + 1;

            $sqlUpdate = "UPDATE discount SET likes = ? WHERE shop_id = ? AND product_id = ?";
            $stmtUpdate = $conn->prepare($sqlUpdate);
            $stmtUpdate->bind_param("iss", $newValue, $spId, $prodId);

            if ($stmtUpdate->execute()) {
                $query = "SELECT current_score FROM user WHERE user_id = ?";
                $stmt = $conn->prepare($query);
                $stmt->bind_param("i", $uid);
                $stmt->execute();
                $result = $stmt->get_result();

                if ($result->num_rows > 0) {
                    $row = $result->fetch_assoc();
                    $currentValue = $row["current_score"];

                    $newValue = $currentValue + 5;

                    $sqlUpdate = "UPDATE user SET current_score = ? WHERE user_id = ?";
                    $stmtUpdate = $conn->prepare($sqlUpdate);
                    $stmtUpdate->bind_param("ii", $newValue, $uid);

                    if ($stmtUpdate->execute()) {
                        echo "Value increased successfully";
                    } else {
                        echo "Error updating record: " . $stmtUpdate->error;
                    }

                    $stmtUpdate->close();
                } else {
                    echo "No records found";
                }
            } else {
                echo "Error updating record: " . $stmtUpdate->error;
            }
        } else {
            echo "No records found";
        }
    } else {
        echo "Product not found";
    }

    $stmt->close();
    $stmtProdId->close();
    $stmtUserId->close();
}
$conn->close();
