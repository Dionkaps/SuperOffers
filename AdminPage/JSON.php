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

        $sqlSelect = "SELECT id,name FROM products WHERE id = ? OR name = ?";
        $sqlInsert = "INSERT INTO products (id, name, category_id, subcategory_id) VALUES ( ?, ?, ?, ?)";
        $sqlUpdate = "UPDATE products SET name = ?, category_id = ?, subcategory_id = ? WHERE id = ?";
        $stmtSelect = $conn->prepare($sqlSelect);
        $stmtInsert = $conn->prepare($sqlInsert);
        $stmtUpdate = $conn->prepare($sqlUpdate);
        
        foreach ($dataArray as $item) {
            // Check if the entry already exists
            $stmtSelect->bind_param("ss", $item['id'],$item['name']);
            $stmtSelect->execute();
            $stmtSelect->store_result();
            
            if ($stmtSelect->num_rows === 0) {
                // Entry doesn't exist, insert it
                $stmtInsert->bind_param("ssss", $item['id'], $item['name'],$item['category_id'], $item['subcategory_id']);
                
                if ($stmtInsert->execute()) {
                    echo "Data inserted successfully!";
                } else {
                    echo "Error: " . $stmtInsert->error;
                }
            } else {// h name yparxei hdh h id yparxei hdh
                $idToUpdate = $item['id'];
                $newName = $item['name']; 
                $newCategoryId = $item['category_id']; 
                $newSubcategoryId =  $item['subcategory_id']; 
                $stmtUpdate->bind_param("ssss", $newName , $newCategoryId ,$newSubcategoryId , $idToUpdate);
                $stmtUpdate->execute();
               echo "Updated successfully!";
            }
        }

        // Close the prepared statements and database connection
        $stmtSelect->close();
        $stmtInsert->close();
        $conn->close();
    } else {
        echo "File upload error: " . $_FILES["fileToUpload"]["error"];
    }
}
?>
