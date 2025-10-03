CREATE DATABASE IF NOT EXISTS ems_db;
USE ems_db;

CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) NOT NULL
);

INSERT INTO employees (name, department, salary) VALUES
('Alice', 'HR', 50000.00),
('Bob', 'IT', 60000.00),
('Charlie', 'Finance', 55000.00);
