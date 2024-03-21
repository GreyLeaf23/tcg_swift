<?php
// Check if both username and password are provided
if(isset($_POST['username']) && isset($_POST['password'])) {
    // Retrieve username and password from POST data
    $username = $_POST['username'];
    $password = $_POST['password'];
    
    // Database connection details
    $host = 'tcg-swift.cng62qqg8t3b.us-east-2.rds.amazonaws.com'; // or your host, e.g., a remote IP or hostname
    $dbname = 'tcg-swift'; // your database name
    $db_username = 'Tcg'; // your database username
    $db_password = '4321Tcg$'; // your database password
    
    // Create connection
    $conn = new mysqli($host, $db_username, $db_password, $dbname);
    
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    // Prepare and execute a query to fetch the user's data based on the provided username
    $stmt = $conn->prepare("SELECT id, username, password FROM Users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();
    
    // Check if the user exists
    if ($result->num_rows > 0) {
        // Fetch user details
        $row = $result->fetch_assoc();
        // Verify password
        if (password_verify($password, $row['password'])) {
            // Password is correct, redirect to success page or perform further actions
            echo "Login successful!";

        } else {
            // Password is incorrect
            echo "Incorrect password!";
        }
    } else {
        // User does not exist
        echo "User not found!";
    }
    
    // Close statement and connection
    $stmt->close();
    $conn->close();
} else {
    // Handle case when username or password is not provided
    echo "Please provide both username and password!";
}
?>
