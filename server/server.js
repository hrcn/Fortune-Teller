const mysql = require('mysql');
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const config = require('./config');

const multer  = require('multer')
const upload = multer({ dest: 'uploads/' })
const fs = require('fs');

const app = express();
app.use(cors());
app.use(bodyParser.urlencoded({ extended: true })); // to support JSON-encoded bodies
app.use(bodyParser.json()); // to support URL-encoded bodies

// connect to MySQL database
const connection = mysql.createConnection(config);

// SQL queries
const INSERT_NEW_USER = 'INSERT INTO user_info SET ?'
const INSERT_NEW_QUESTION = 'INSERT INTO user_question SET ?';
const INSERT_NEW_FACE = 'INSERT INTO user_face (faceImage) VALUES (?)';
const INSERT_NEW_HAND = 'INSERT INTO user_hand (handImage) VALUES (?)';

// add new user to MySQL database
app.post('/api/newuser', (req, res) => {
    const data = req.body;
    connection.query(INSERT_NEW_USER, data, (error, results) => {
        if (error) throw error;
        res.end(JSON.stringify(results));
    });
});

// add new question to MySQL
app.post('/api/newquestion', (req, res) => {
    const data = req.body;
    connection.query(INSERT_NEW_QUESTION, data, (error, results) => {
        if (error) throw error;
        res.end(JSON.stringify(results));
    });
});

// add new user face image to MySQL database
app.post('/api/newface', upload.single('faceImage'), (req, res) => {
    const faceImage = req.file;
    fs.readFile(faceImage.path, (err, data) => {
        connection.query(INSERT_NEW_FACE, data, (error, results) => {
            if (error) throw error;
            res.end(JSON.stringify(results));
        })
    })
});

// add new user hand image to MySQL database
app.post('/api/newhand', upload.single('handImage'), (req, res) => {
    const faceImage = req.file;
    fs.readFile(faceImage.path, (err, data) => {
        connection.query(INSERT_NEW_HAND, data, (error, results) => {
            if (error) throw error;
            res.end(JSON.stringify(results));
        })
    })
});

// connect Express to MySQL
connection.connect((err) => {
    if(err) {
        return console.error(err.message);
    } else {
        console.log("Server Connected!")
    }
});

const port = 4000;
app.listen(port, () => console.log('Server started and listening on ' + port));