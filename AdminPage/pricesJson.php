<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "webdev";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if there was no file upload error
    if ($_FILES["fileToUpload2"]["error"] === UPLOAD_ERR_OK) {
        // Read JSON data from the uploaded file
        $jsonData = file_get_contents($_FILES["fileToUpload2"]["tmp_name"]);

        // Decode JSON data into an associative array
        $dataArray = json_decode($jsonData, true);

        $conn = new mysqli($servername, $username, $password, $dbname);

        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        $sqlInsert = "INSERT INTO prices (product_id, price, date) VALUES ( ?, ?, ?)";
        $stmtInsert = $conn->prepare($sqlInsert);
        $currentDate = date("Y-m-d");

        foreach ($dataArray as $item) {
            //Insert new price
            $stmtInsert->bind_param("sss", $item['id'], $item['price'], $currentDate);

            if ($stmtInsert->execute()) {
                echo "Insert";
            } else {
                echo "Error: " . $stmtInsert->error;
            }
        }

        // Close the prepared statements and database connection
        $stmtInsert->close();
        $conn->close();
    } else {
        echo "File upload error: " . $_FILES["fileToUpload2"]["error"];
    }
}
