DROP DATABASE IF EXISTS mydb;
CREATE DATABASE mydb;
USE mydb;
CREATE TABLE product_versions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    version VARCHAR(255) NOT NULL
                    );
INSERT INTO product_versions (name, version) VALUES ('MySQL', '8');
