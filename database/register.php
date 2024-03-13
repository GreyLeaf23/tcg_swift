<?php
// Define database connection parameters
$host = 'localhost'; // or your host, e.g., a remote IP or hostname
$dbname = 'TCG_Swift';
$username = 'db_username'; // your database username
$password = 'db_password'; // your database password

// Create connection
$conn = new mysqli($host, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve username and password from POST data and sanitize them
$username = $conn->real_escape_string($_POST['username']);
$password = $conn->real_escape_string($_POST['password']);

// Hash passwords before storing them
$hashed_password = password_hash($password, PASSWORD_DEFAULT);

// Prepare and bind
$stmt = $conn->prepare("INSERT INTO Users (username, password) VALUES (?, ?)");
$stmt->bind_param("ss", $username, $hashed_password);

// Execute the prepared statement
if ($stmt->execute()) {
    echo "New record created successfully";
} else {
    echo "Error: " . $stmt->error;
}

// Close statement and connection
$stmt->close();
$conn->close();
?>
