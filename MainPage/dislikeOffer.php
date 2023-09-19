<?php
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $jsonData = file_get_contents("php://input");
    $data = json_decode($jsonData, true);
    $spId = $data['spid'];
    $pName = $data['pname'];
    $uid = $data['userid'];

    $queryProdId = "SELECT id FROM products WHERE name = ?";
    $stmtProdId = $conn->prepare($queryProdId);
    $stmtProdId->bind_param("s", $pName);
    $stmtProdId->execute();
    $resultProdId = $stmtProdId->get_result();

    if ($resultProdId->num_rows > 0) {
        $row = $resultProdId->fetch_assoc();
        $prodId = $row['id'];

        $query = "SELECT dislikes FROM discount WHERE shop_id = ? AND product_id = ?";
        $stmt = $conn->prepare($query);
        $stmt->bind_param("ss", $spId, $prodId);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows > 0) {
            $row = $result->fetch_assoc();
            $currentValue = $row["dislikes"];

            $newValue = $currentValue + 1;

            $sqlUpdate = "UPDATE discount SET dislikes = ? WHERE shop_id = ? AND product_id = ?";
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

                    //User score cannot be negative
                    if ($currentValue > 0) {
                        $newValue = $currentValue - 1;
                    } else {
                        $newValue = $currentValue;
                    }

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
}
$conn->close();
