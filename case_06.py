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
