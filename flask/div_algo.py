import numpy as np 
import pandas as pd
import cv2
import pickle


kpts = np.load("result.npy")

eyebow_dis = kpts[23][0] - kpts[22][0]#(1-30)
upperface = (kpts[28][1] - (kpts[20][1]+kpts[25][1])/2)*2
midface = kpts[34][1]-kpts[28][1]
botFace = kpts[9][1]-kpts[34][1]
wholeFace = upperface+midface+botFace

nosew = kpts[36][0]-kpts[32][0]
noseH = kpts[24][1] - (kpts[32][1]+kpts[31][1])/2

mouth = kpts[55][0]-kpts[49][0]
faceWidth = kpts[17][0]-kpts[1][0]


eyebow_score = abs((eyebow_dis/faceWidth)*10-25)
nose_score = abs((nosew/faceWidth)-25) + abs((noseH/faceWidth)-50)/4
mouth_score = abs((mouth/faceWidth)*10-50)


face_score = eyebow_score+nose_score+mouth_score
print(face_score)

if face_score > 100:
    face_score = 100
elif face_score < 0:
    face_score = 0

print(face_score)