<?php
  //connect to mysql db
  $conn = mysqli_connect("localhost", "root", "", "web") or die('Could not connect: ' . mysqli_error($conn));

  
  //read the json file contents
  $jsondata = file_get_contents('categories.json');
  
  //convert json object to php associative array
  $data = json_decode($jsondata, true);

  $stmt = $conn->prepare("
  INSERT INTO category(category_id, category_name)
  VALUES(?,?)
");

$stmt->bind_param("ss", $category_id, $category_name);
/*
$stmt2 = $conn->prepare("
  INSERT INTO subcategory(subcategory_id, subcategory_name)
  VALUES(?,?,?)
");

$stmt->bind_param("sss", $subcategory_id, $subcategory_name, $category_id);
*/
$categories = $data['categories'];


foreach ($categories as $category) {
    $category_id = $category["id"];
    $category_name = $category["name"];
    
    $stmt->execute();
    /*
    $subcategories = $categories['subcategories'];

    foreach ($subcategories as $subcategory) {
        $subcategory_id = $subcategory["uuid"];
        $subcategory_name = $subcategory["name"];
   } 

   $stmt2->execute();*/
}
 
if($stmt){
    echo "Imported data succesfully!";
}
else{
    echo "Data import failed.";
}


?>