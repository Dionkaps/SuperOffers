<?php
session_start();

if (isset($_SESSION['user_id'])) {
    $user_id = $_SESSION['user_id'];

    // Replace these values with your database connection details
    $conn = new mysqli('localhost', 'root', '', 'webdev');

    if ($conn->connect_error) {
        echo json_encode(array('status' => 'error', 'message' => 'Connection Failed: ' . $conn->connect_error));
        exit;
    } else {
        $sql = "SELECT product_id, shop_id, date FROM rating WHERE user_id='$user_id'";
        $result = mysqli_query($conn, $sql);

        if ($result) {
            $offerData = array(); // Initialize an empty array

            while ($row = mysqli_fetch_assoc($result)) {
                $prodId = $row['product_id'];
                $shopId = $row['shop_id'];
                $date = $row['date'];

                // Fetch product name
                $query1 = "SELECT name FROM products WHERE id = ?";
                $stmt1 = $conn->prepare($query1);
                $stmt1->bind_param("s", $prodId);
                $stmt1->execute();
                $result1 = $stmt1->get_result();

                if ($result1 && $productRow = $result1->fetch_assoc()) {
                    $productName = $productRow['name'];
                } else {
                    echo "Error executing the first query: " . $conn->error;
                }

                // Fetch shop name
                $query2 = "SELECT name FROM shop WHERE shop_id = ?";
                $stmt2 = $conn->prepare($query2);
                $stmt2->bind_param("s", $shopId);
                $stmt2->execute();
                $result2 = $stmt2->get_result();

                if ($result2 && $shopRow = $result2->fetch_assoc()) {
                    $shopName = $shopRow['name'];
                } else {
                    echo "Error executing the second query: " . $conn->error;
                }

                // Add the data to the offerData array
                $offerData[] = array(
                    'productName' => $productName,
                    'shopName' => $shopName,
                    'date' => $date
                );
            }

            echo json_encode(array('status' => 'success', 'odata' => $offerData));
        } else {
            echo json_encode(array('status' => 'error', 'message' => 'Failed to fetch offer data.'));
        }

        $conn->close();
    }
} else {
    echo json_encode(array('status' => 'error', 'message' => 'User not authenticated.'));
}
