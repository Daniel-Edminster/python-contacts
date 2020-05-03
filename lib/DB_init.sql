--Database initialization
CREATE DATABASE `contacts`;
CREATE TABLE `my_contacts` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `phone_number` int(10) NOT NULL
);
