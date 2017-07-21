#Keras model
#------------------------------------------
from keras.models import Sequential
from keras.layers import Dense, Activation

x_train = list('1234567890')
y_train = list('MFASTYUIOP')

x_test = list('1234')
y_test = list('MFIU')

model = Sequential()

model.add(Dense(units=64, imput_dim=100))
model.add(Activation('relu'))
model.add(Dense(units=10))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, batch_size=32)

print(model.evaluate(x_test, y_test, batch_size=128)[1])

#Tensofflow model
#------------------------------------------
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

FLAGS = None

def main(_):
	mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

	for _ in range(1000):
		batch_xs, batch_ys = mnist.train.next_batch(100)
		sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})

	x = tf.placeholder(tf.float32, [None, 784])
	W = tf.Variable(tf.zeros([784, 10]))
	b = tf.Variable(tf.zeros([10]))
	y = tf.matmul(x, W) + b

