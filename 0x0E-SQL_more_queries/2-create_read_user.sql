-- creates the database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE IF NO EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'IDENTIFIED BY 'user_0d_1_pwd';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
