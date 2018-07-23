import tensorflow as tf
import numpy as np
import random
from PIL import Image
from tensorflow.examples.tutorials.mnist import input_data
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


sess = tf.Session()
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)
