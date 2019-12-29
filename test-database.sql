CREATE DATABASE IF NOT EXISTS `test`;

-- ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'e124676136'

USE test;

DROP TABLE IF EXISTS `user_info`;
CREATE TABLE user_info (
	name VARCHAR(255),
    gender VARCHAR(6),
    phone INT,
    birthday DATE,
    constellation VARCHAR(255)
);

DROP TABLE IF EXISTS `user_question`;
CREATE TABLE user_question (
	question VARCHAR(255)
);

DROP TABLE IF EXISTS `user_face`;
CREATE TABLE user_face (
	faceImage LONGBLOB
);

DROP TABLE IF EXISTS `user_hand`;
CREATE TABLE user_hand (
	handImage LONGBLOB
);

