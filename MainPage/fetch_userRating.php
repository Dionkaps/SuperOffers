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
                $offerData[] = $row; // Add each row to the array
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
?>
