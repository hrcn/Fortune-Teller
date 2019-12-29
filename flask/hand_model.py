import tensorflow as tf
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import cv2
import pickle
from flask import Response
import io
import base64


#input_img = cv2.imread('06000.jpg')

def run_model(input_img):
    img_h,img_w,img_c = input_img.shape
    first_line = [[270,360],[482,432]]
    second_line = [[189,396],[462,514.5]]
    third_line = [[178.2,576],[300,576]]
    
    
    
    fig = Figure(figsize=(3, 3))
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    ax.imshow(input_img)
    ax.plot(first_line[0], first_line[1], 'red', linestyle=':', marker='')
    ax.plot(second_line[0], second_line[1], 'red', linestyle=':', marker='')
    ax.plot(third_line[0], third_line[1], 'red', linestyle=':', marker='')
    ax.axis('off')

    canvas.draw() 
    buf = fig.canvas.tostring_rgb()
    ncol, nrows = fig.canvas.get_width_height()
    
    return np.fromstring(buf, dtype=np.uint8).reshape((ncol,nrows,3))




