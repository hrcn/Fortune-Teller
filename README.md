# Fortune-Teller

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

ALTER TABLE users MODIFY COLUMN UserId INT(20) AUTO_INCREMENT; ALTER TABLE users AUTO_INCREMENT = 1;

### Run Client 

`cd client `

`npm install`

`npm start`

### Run Express 

`cd server`

`npm install` 

`nodemon server.js`

### Run Flask

`cd flask-backend`
`python api.py`
