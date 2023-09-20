<?php
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'webdev';
$flag = 0;

// Create a database connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL query to select 'product_id' and 'discount_price' columns from the 'discount' table
$sql = "SELECT product_id, discount_price, shop_id FROM discount";

// Execute the query
$result = $conn->query($sql);

// Check if there are any results
if ($result->num_rows > 0) {
    // Calculate the date one week ago from the current date
    $oneWeekAgo = date('Y-m-d', strtotime('-1 week'));
    $startDate = $oneWeekAgo;
    $endDate = date('Y-m-d');
    // Output data for each row
    while ($row = $result->fetch_assoc()) {
        $productId = $row["product_id"];
        $discountPrice = $row["discount_price"];
        $shopId = $row["shop_id"];

        // Fetch the most recent price for the product from the 'prices' table
        $query = "SELECT price FROM prices WHERE product_id = ? ORDER BY date DESC LIMIT 1";
        $stmt = $conn->prepare($query);
        $stmt->bind_param("s", $productId);
        $stmt->execute();
        $priceResult = $stmt->get_result();

        if ($priceResult->num_rows > 0) {
            $priceRow = $priceResult->fetch_assoc();
            $currentPrice = $priceRow["price"];

            // Check if the discount price is less than 80% of the current price
            if ($discountPrice < 0.8 * $currentPrice) {
                echo "Product ID: " . $productId . "<br>";
                echo "Discount Price: " . $discountPrice . "<br>";
                echo "Most Recent Price: " . $currentPrice . "<br>";
                echo "Discount price is less than 80% of the current price.<br>";
                echo "<hr>"; // Separation line between records
                $flag = 0;
            } else {
                $flag = $flag + 1;
            }
        } else if ($discountPrice >= 0.8 * $currentPrice) {
            echo "No records found for the most recent price.<br>";
            echo "<hr>"; // Separation line between records
        }

        // Modify the query to calculate the average price for the past week
        $query = "SELECT AVG(price) AS average_price FROM prices WHERE product_id = ? AND date >= ? AND date <= ?";
        $stmt = $conn->prepare($query);

        // Bind the variables
        $stmt->bind_param("sss", $productId, $startDate, $endDate);

        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows > 0) {
            $row = $result->fetch_assoc();
            $averagePrice = $row["average_price"];
            if ($discountPrice < 0.8 * $averagePrice) {
                echo "Product ID: " . $productId . "<br>";
                echo "Discount Price: " . $discountPrice . "<br>";
                echo "Most Recent Price: " . $averagePrice . "<br>";
                echo "Discount price is less than 80% of the average price.<br>";
                echo "<hr>"; // Separation line between records
                $flag = 0;
            } else if ($discountPrice >= 0.8 * $averagePrice) {
                $flag = $flag + 1;
            }
        } else {
            echo "No records found for the past week";
        }

        if ($flag == 2) {
            // Delete the row from the 'discount' table
            $deleteQuery = "DELETE FROM discount WHERE product_id = ? AND shop_id = ?";
            $deleteStmt = $conn->prepare($deleteQuery);
            $deleteStmt->bind_param("ss", $productId, $shopId);
            $deleteStmt->execute();
            $deleteStmt->close();
            $flag = 0;
        }
        else {
            echo "No records found for the past week";
        }
        $stmt->close();
    }
} else {
    echo "No records found in the 'discount' table.";
}

// Close the database connection
$conn->close();
