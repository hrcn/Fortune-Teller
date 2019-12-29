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




def run(input_img):

    sess = tf.Session()
    # img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    img = np.float32(input_img)
    img = cv2.resize(img, (224, 224))
    img = img/127.5 - 1
    img = tf.convert_to_tensor(img)
    img = tf.reshape(img,(1,224,224,1))
    i = sess.run(tf.squeeze(img))


    def c2c(hm,n=5):
        ind = hm.argsort(axis=None)[-n:]
        topind = np.unravel_index(ind,hm.shape)

        i0,i1,hsum = 0,0,0
        for indx in zip(topind[0],topind[1]):
            h = hm[indx[0],indx[1]]
            hsum += h
            i0 += indx[0]*h
            i1 += indx[1]*h
    
        i0 /= hsum
        i1 /= hsum
        return [i1,i0]

    def show(a, b):

        #save a plot figure as png
        #ax = plt.subplot('111')
        #plt.xlabel('X Axis', axes=ax)
        #plt.ylabel('Y Axis', axes=ax)
        #ax.imshow(a)
        #ax.scatter(b[:, 0], b[:, 1], s=20, marker='.', c='m')
        #plt.savefig('test.png', bbox_inches="tight")


        fig = Figure(figsize=(3, 3))
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.imshow(a)
        ax.scatter(b[:, 0], b[:, 1], s=20, marker='.', c='m')
        ax.axis('off')
        
        canvas.draw() 
        buf = fig.canvas.tostring_rgb()
        ncol, nrows = fig.canvas.get_width_height()
        return np.fromstring(buf, dtype=np.uint8).reshape((ncol,nrows,3))


        
    
    def show_plot(a,b):
        plt.imshow(a)
        plt.scatter(b[:, 0], b[:, 1], s=20, marker='.', c='m')
        


    def cd(hm):
        assert len(hm.shape) == 3
        Nlandmarks = hm.shape[-1]
        est_xy = []
        for i in range(Nlandmarks):
            hmi = hm[:,:,i]
            est_xy.append(c2c(hmi))
    
        return np.array(est_xy)


    with tf.variable_scope('conv1') as scope:
        m = tf.nn.conv2d(img,tf.get_variable(name = 'filter',shape = [3,3,1,16]),strides =(1,1,1,1),padding ="SAME") + tf.get_variable(name = 'bias', shape = [16])

    with tf.variable_scope('bn1') as scope:
        m = tf.nn.relu(tf.layers.batch_normalization(inputs = m,axis = -1,momentum = 0.9,epsilon = 0.001,center = True,scale = True,
                                                        training = False))

    with tf.variable_scope('conv2') as scope:
        m = tf.nn.conv2d(m,tf.get_variable(name = 'filter',shape = [3,3,16,64]),strides =(1,1,1,1),padding ="SAME") + tf.get_variable(name = 'bias', shape = [64])

    with tf.variable_scope('bn2') as scope:
        m = tf.nn.relu(tf.layers.batch_normalization(inputs = m,axis = -1,momentum = 0.9,epsilon = 0.001,center = True,scale = True,
                                                        training = False))

    with tf.variable_scope('conv3') as scope:
        m = tf.nn.conv2d(m,tf.get_variable(name = 'filter',shape = [3,3,64,64]),strides =(1,2,2,1),padding ="SAME") + tf.get_variable(name = 'bias', shape = [64])


    with tf.variable_scope('bn3') as scope:
        m = tf.nn.relu(tf.layers.batch_normalization(inputs = m,axis = -1,momentum = 0.9,epsilon = 0.001,center = True,scale = True,
                                                        training = False))

    with tf.variable_scope('conv4') as scope:
        m = tf.nn.conv2d(m,tf.get_variable(name = 'filter',shape = [3,3,64,128]),strides =(1,2,2,1),padding ="SAME") + tf.get_variable(name = 'bias', shape = [128])

    with tf.variable_scope('bn4') as scope:
        m = tf.nn.relu(tf.layers.batch_normalization(inputs = m,axis = -1,momentum = 0.9,epsilon = 0.001,center = True,scale = True,
                                                        training = False))

    with tf.variable_scope('conv5') as scope:
        m = tf.nn.conv2d(m,tf.get_variable(name = 'filter',shape = [3,3,128,160]),strides =(1,1,1,1),padding ="SAME") + tf.get_variable(name = 'bias', shape = [160])

    with tf.variable_scope('bn5') as scope:
        m = tf.nn.relu(tf.layers.batch_normalization(inputs = m,axis = -1,momentum = 0.9,epsilon = 0.001,center = True,scale = True,
                                                        training = False))

    with tf.variable_scope('bottleneck') as scope:
        m = tf.nn.conv2d(m,tf.get_variable(name = 'filter',shape = [7,7,160,160]),strides =(1,1,1,1),padding ="SAME") + tf.get_variable(name = 'bias', shape = [160])

    with tf.variable_scope('bn6') as scope:
        m = tf.nn.relu(tf.layers.batch_normalization(inputs = m,axis = -1,momentum = 0.9,epsilon = 0.001,center = True,scale = True,
                                                        training = False))

    with tf.variable_scope('dconv6') as scope:
        pred = tf.nn.conv2d_transpose(value = m,filter = tf.get_variable(name = 'filter',shape=[4,4,68,160]),output_shape = [1,224,224,68],strides = (1,4,4,1))+tf.get_variable(name='bias',shape = [68])
        



    saver = tf.train.Saver()
    saver.restore(sess,"face_pt_testing_heat_map1.ckpt")
    hm = sess.run(tf.squeeze(pred))
    out = cd(hm)
    np.save("result.npy",out)

    #plt.figure(figsize=(5, 5))
    response = show(i, out)
    #show_plot(i,out)
    #plt.show()

    return response


# if __name__ == "__main__":
#     res = run("test_image1.jpeg")
#     print(repr(res))
    

