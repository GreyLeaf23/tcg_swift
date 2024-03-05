<?php
// Assuming you have established a database connection

// Retrieve data from form submission
$username = $_POST['username'];
$password = $_POST['password']; // Note: Hash and salt the password for security

// Insert data into the database
$sql = "INSERT INTO Users (username, password) VALUES ('$username', '$password')";
if (mysqli_query($conn, $sql)) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

// Close the database connection
mysqli_close($conn);
?>
