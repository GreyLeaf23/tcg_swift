// Import required modules and configuration
const mysql = require('mysql');
const dbConfig = require('./config');

// Create a connection pool
const pool = mysql.createPool(dbConfig);

// Test the connection
pool.getConnection((err, connection) => {
    if (err) {
        console.error('Error connecting to database:', err);
        return;
    }
    console.log('Connected to the database');
    connection.release(); // Release the connection
});

