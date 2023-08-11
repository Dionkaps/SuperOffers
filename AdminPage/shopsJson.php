<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "webdev";

if (isset($_POST["submit"])) {
    // Check if there was no file upload error
    if ($_FILES["fileToUpload"]["error"] === UPLOAD_ERR_OK) {
        // Read JSON data from the uploaded file
        $jsonData = file_get_contents($_FILES["fileToUpload"]["tmp_name"]);

        // Decode JSON data into an associative array
        $dataArray = json_decode($jsonData, true);

        $conn = new mysqli($servername, $username, $password, $dbname);

        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        $sqlSelect = "SELECT shop_id,name FROM shop WHERE shop_id = ? OR name = ?";
        $sqlInsert = "INSERT INTO shop (shop_id, name) VALUES ( ?, ?)";
        $sqlUpdate = "UPDATE shop SET name = ?, shop_id = ?  WHERE shop_id = ?";
        $stmtSelect = $conn->prepare($sqlSelect);
        $stmtInsert = $conn->prepare($sqlInsert);
        $stmtUpdate = $conn->prepare($sqlUpdate);

        foreach ($dataArray as $item) {
            // Check if the entry already exists
            $stmtSelect->bind_param("ss", $item['shop_id'], $item['name']);
            $stmtSelect->execute();
            $stmtSelect->store_result();

            if ($stmtSelect->num_rows === 0) {
                // Entry doesn't exist, insert it
                $stmtInsert->bind_param("ss", $item['shop_id'], $item['name']);

                if ($stmtInsert->execute()) {
                    echo "Data inserted successfully!";
                } else {
                    echo "Error: " . $stmtInsert->error;
                }
            } else { // h name yparxei hdh h id yparxei hdh
                $idToUpdate = $item['shop_id'];
                $newName = $item['name'];
                $stmtUpdate->bind_param("ss", $newName, $idToUpdate);
                $stmtUpdate->execute();
                echo "Updated successfully!";
            }
        }

        // Close the prepared statements and database connection
        $stmtSelect->close();
        $stmtInsert->close();
        $stmtUpdate->close();
        $conn->close();
    } else {
        echo "File upload error: " . $_FILES["fileToUpload"]["error"];
    }
}
