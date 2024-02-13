const mysql = require('mysql');

const pool = mysql.createPool({
  connectionLimit: 10,
  host: 'localhost',
  user: 'daggz',
  password: 'smoothoperator',
  database: 'tcg_data' // Updated database name
});
