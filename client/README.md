ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

ALTER TABLE users MODIFY COLUMN UserId INT(20) AUTO_INCREMENT;
ALTER TABLE users AUTO_INCREMENT = 1;

1. Install Node.js
https://nodejs.org/en/

2. Run Client
cd client
npm install
npm start

3. Run Server
cd server
npm install
nodemon server.js
