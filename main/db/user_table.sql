CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,  -- Storing the user's first name
    last_name VARCHAR(100) NOT NULL,   -- Storing the user's last name
    email VARCHAR(100) UNIQUE NOT NULL,  -- Storing the user's email (unique)
    password_hash VARCHAR(255) NOT NULL,  -- Storing the hashed password
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Automatically storing the creation timestamp
);
