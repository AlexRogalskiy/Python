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

#Tensorflow model
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

#Bin Numeric Variables to Categoricals
#------------------------------------------
# Create a list of 20 integers between 1 and 100
var = np.random.random_integers(1, 100, 50)
print var[:10], '\n'
# Default: cut the data into 3 bins of equal size
cats = pd.cut(var, 4)
print cats.categories,'\n'
print cats.labels,'\n'
#Display the Series and the category
print pd.concat([Series(var), Series(cats)], axis=1).ix[:10,]

#Create Dummy Variables
#------------------------------------------
df_G = DataFrame({'key': list('bbacccb'),
                  'val': np.arange(7) })
# Create the dummy variable matrix
pd.get_dummies(df_G['key'], prefix='dummy')
# Create and merge dummies in the same DF
df_G.join(pd.get_dummies(df_G['key'], prefix='dummy'))

# Create a categorical variable from a numeric and then compute dummies
df_G.val = np.random.rand(7)
df_G.join(pd.get_dummies(pd.cut(df_G['val'], 3, labels=list('abc')), prefix='dummy'))

#Random Sampling
#------------------------------------------
# Create a toy dataset
df = DataFrame(np.random.randn(1000, 5), columns=list('ABCDE'))
df[:10]

# Without Replacement
# Create a randomized index equal to the length of the DF
sample = np.random.permutation(len(df))

# Subset it to retain only the desired number of cases
train = sample[:np.around(len(df) * 0.7)]

# Index the DF using this
train = df.ix[train]
print len(train), '\n', train.head()

# With Replacement
repl = np.random.randint(0, 1000, 700)
Series(repl).value_counts().head()

#Plot datasets
#------------------------------------------
# UNIVARIATE data
s = Series(np.random.randn(100).cumsum())
s.plot()
s.plot(kind='line',
       grid=False, legend=True,
       label='timeseries',
       xlim=(0, 100), ylim=(-5, 15),
       xticks=np.arange(0, 100, 15), yticks=np.arange(-2, 15, 2),
       style='b--', alpha=0.7 )

s.plot(kind='hist', bins=15, color='k', alpha=0.4, title='A histogram')

#MULTIVARIATE data
df = DataFrame(np.random.randn(5,5), index=list('ABCDE'), columns=list('PQRST'))
print df

# Default plot
df.cumsum().plot()

df.cumsum().plot(figsize=(10, 5),
                   title='plot of 5 time series',
                  legend=False)

df.plot(kind='line',
        figsize=(8, 12),
        title='Each variable is now on its own plot, but the axes are shared',
        color='b',
        subplots=True, sharex=True, sharey=True)

s = Series(np.random.rand(10), index=list('abcdefghij'))
s.plot(kind='bar', ax=axes[0], color='k', alpha=0.6) #kind=barh (for horiz bars)

df = DataFrame(np.random.rand(5,5), index=list('ABCDE'), columns=list('PQRST'))
print df
df.plot(kind='bar', stacked=True, alpha=0.5)

# Using Gaussian data
Series(np.random.randn(1000)).hist(bins=30, alpha=0.4)
# Using counts data
Series(np.random.randint(1, 100, 1000)).plot(kind='hist', bins=30, color='Y')
# Density Plot
Series(np.random.randn(1000)).plot(kind='kde')
# Overlay a density curve on a histogram (data are bimodal)
s1 = np.random.normal(0, 1, 200)
s2 = np.random.normal(9, 2, 200)
v = Series(np.concatenate([s1, s2]))
 v.hist(bins=100, alpha=0.4, color='M', normed=True)
v.plot(kind='kde', style='k--')


# Scatter Plot
# Create a dataset
df = DataFrame({'A': np.arange(50),
                'B': np.arange(50) + np.random.randn(50),
                'C': np.sqrt(np.arange(50)) + np.sin(np.arange(50)) })
# Two variable Scatterplot
plt.scatter(df['B'], df['C'])
plt.title('Scatterplot of X+epsilon - and - sqrt(x)+sin(x)')
#Scatterplot Matrix
pd.scatter_matrix(df)

#SciPy workshow
#------------------------------------------
import numpy as np
from scipy import signal

numpy.loadtxt()OR numpy.savetxt()

from scipy import misc
misc.imread(‘Image_Name.png’)

from scipy import linalg
mat = np.array([[2,1],[4.3]])    #For a square matrix ‘mat’
linalg.det(mat)					 #only works on Square Matrix.

#not work for Singular matrix, because its determinant is zero
linalg.inv(sqr_mat)    #For a square matrix ‘sqr_mat’

linalg.svd(mat)    #Returns 3 arguments after Singular Value Decomposition


# To calculate the area under a Guassian curve, we use erf() function like this:
scipy.special.erf()
# Syntax for Gamma function:
scipy.special.gamma()
# In order to calculate the log of Gamma, we use the following syntax:
scipy.special.gammaln()
# Elliptic Function
scipy.special.eppilj()
# Nth order Bessel Function
scipy.special.jn()


from scipy import optimize
def f(x):    #Defining function
	return   x**3 + x**2 + np.sin(x) +np.cos(x)
x = np.arrange(-50, 50, 0.01)
#First two arguments are the limit and the last argument is the interval
plt.plot(x, f(x))
plt.show()    #To show the graph of the defined function

#This algorithm calculates a gradient descent of the function from the starting point given in the argument and outputs the minima with zero gradient and positive second order derivative
optimize.fmin_bfgs(f, o)
#First argument is function’s name and second argument is the starting point of gradient descent

# combines a local optimizer with stochastic sampling of starting points for the local optimizer, hence giving a costlier global minimum. The syntax to use this function is as follows:
optimize.basinhopping(f, 0)
#Brute force method can also be used for global optimization, but it is less efficient
optimize.brute(f, 0)
#find the local minimum within an interval for variables
optimize.fminbound(f, -50, 50)    #Argument is interval for the variable.

#estimate the roots of a scalar function by finding the solution of the equation; f(x) = 0
roots = optimize.fsolve(f)

#using least squares curve fitting
x_data = np.linspace(-100, 100, 0.1)
y_data = g(x_data)+ np.random.randn(x_data.size)


def h(x, a, b):
	return a*x + b*np.cos(x)
initial_guess_ab = [1, 1]
variables, variables_covariance = optimize.curve_fit(h, x_data, y_data, initial_guess_ab)

#Fourier Transformation is computed on a time domain signal to check its behaviour in frequency domain
signal = np.sin(x +10)
x = np.linspace(-100, 100, 0.1)
time_step = 0.01

#Since the signal is a real function, its fourier transform will be symmetric
from scipy import fftpack
sampling_frequency = fftpack.fftfreq(signal.size, d=time_step)
signal_fft = fftpack.fft(signal)

#Similarly an inverse Fourier transform can be computed
original_signal = fftpack.ifft(signal_fft)

from scipy.integrate import quad
result, error = quad(np.sin, 0, np.pi/2)

def derivative_equation(x, time):
	return 10 * time
from scipy.integrate import odeint
time_step = np.linspace(0, 10, 100)    #Time step is 0.1 from [0, 100)
x_value, info = odeint(derivative_equation, 1, time_step)


from scipy import ndimage
ndimage.shift(image, (x, y))    #Shifting Image with (x, y) coordinate
ndimage.rotate(image, angle)    #Rotating image to that angle
ndimage.zoom(image, magnitude)  #Zooming image with the magnitude

ndimage.median_filter(image, argument)            #Filtering image using Median filter
ndimage.gaussian_filter(image, argument)          #Filtering image using Gaussian filter

ndimage.binary_erosion(image)           #Binary Erosion on image
ndimage.binary_dilation(image)          #Binary Dilation on image
ndimage.binary_opening(image)           #Binary Opening on image
ndimage.binary_closing(opened_image)    #Binary Closing on opened image

#Resampling using Fourier transform
t = np.linspace(-10, 10, 200)    #Defining Time Interval
y = np.sin(t)
signal.resample(y, 100)          # Number of required samples is 100

#Removing Linear Trend
t = np.linspace(-10, 10, 200)    #Defining Time Interval
y = np.sin(t) + t
signal.detrend(y)                # To remove the linear‘t’ variable in the equation