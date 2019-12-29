from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin

import cv2
import numpy as np
import base64
import io

# from test import hello, process_face_image

from run import run # face model
from run_score import score
from hand_model import run_model # hand model
from Predict_func import generate_text

app = Flask(__name__)
cors = CORS(app)

face_score = 0

@app.route("/", methods=['GET'])
def home():
    return hello()

@app.route("/api/newquestion", methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def get_user_question():
    data = request.get_json()
    question = data['question']
    result = generate_text(question, face_score)
    return jsonify(result) 

@app.route("/api/newface", methods=['POST'])
@cross_origin()
def get_user_face():
    global face_score
    img_file = request.files['faceImage']
    f = img_file.stream.read()
    bin_data = io.BytesIO(f)
    file_bytes = np.asarray(bytearray(bin_data.read()), dtype=np.uint8)
    
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # res_img = run(gray_img)
    img_score, res_img = score(gray_img)
    print(img_score)
    face_score = img_score
    retval, buffer = cv2.imencode('.png', res_img)
    jpg_as_text = base64.b64encode(buffer)
    return Response(response=jpg_as_text, content_type='image/jpeg')

@app.route("/api/newhand", methods=['POST'])
@cross_origin()
def get_user_hand():
    img_file = request.files['handImage']
    f = img_file.stream.read()
    bin_data = io.BytesIO(f)
    file_bytes = np.asarray(bytearray(bin_data.read()), dtype=np.uint8)
    
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res_img = run(gray_img)
    retval, buffer = cv2.imencode('.png', res_img)
    jpg_as_text = base64.b64encode(buffer)
    return Response(response=jpg_as_text, content_type='image/jpeg')

app.run(port=5000, debug=True)