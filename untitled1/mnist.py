import cv2 as cv
import math
import numpy as np
import tensorflow as tf
import scipy.misc
import os
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)
save_dir = 'MNIST_data/raw/'
if os.path.exists(save_dir) is False:
    os.makedirs(save_dir)
for i in range(20):
    image_array = mnist.image[i, :]
    image_array = image_array.reshape(28, 28)
    filename = save_dir + 'mnist_train_%d.jpg' % i
    scipy.misc.toimage(image_array, cmin=0.0, cmax=1.0).save(filename)
print(mnist.train.labels[0, :])
for i in range(20):
    one_hot_label = mnist.train.labels[i, :]
    label = np.argmax(one_hot_label)
    print('mnist_train_%d.jpg label: %d' % (i, label))