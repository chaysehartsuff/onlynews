CREATE DATABASE IF NOT EXISTS onlydatabase;
USE onlydatabase;

CREATE TABLE IF NOT EXISTS tournaments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    prize_pool DECIMAL(15,2),
    valid BOOLEAN NOT NULL DEFAULT FALSE
);