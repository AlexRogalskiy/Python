import matplotlib.pyplot as plt

y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]


#Matplot methods
#------------------------------------------
plt.plot(tv, sales)
plt.xlabel('TV')
plt.ylabel('Sales')
plt.title('Advertisement effect on sales')
plt.show()

plt.plot(tv,sales, marker='o', linestyle='--', color='r',label='tv')
plt.plot(radio,sales, marker='*', linestyle='-', color='g', label='raddio')
plt.xlabel('Advertisement medium')
plt.ylabel('Sales')
plt.title('Advertisement effect on sales')
plt.legend(loc='lower right')
plt.show()

## create Random numbers
import numpy as np
x = np.random.randn(1, 50)
y = np.random.randn(1,50)
plt.scatter(x1, y, color='red', s=30) ## here s is size of point in scatter plot
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Scatter Plot')
plt.show()

fig = plt.figure()
## here 1 show number of row, 2 show number of column and 1 show number of subplot
##Left plot
img1 = fig.add_subplot(121)
N=50
x = np.random.randn(N)
y = np.random.randn(N)
colors = np.random.rand(N)
size =(10 * np.random.rand(N))**2 
plt.scatter(x, y, s=size, c=colors, alpha=0.5)

## right plot
img2 = fig.add_subplot(122)
N=100
x1 = np.random.randn(N)
y1 = np.random.randn(N)
area= (15 * np.random.rand(N))**2 
colors = ['red', 'blue', 'green', 'yellow']
plt.scatter(x1, y1, s=area, c=colors, alpha=0.2)
img2.grid(True)## show grid in plot
plt.show()

## Generate gaussian number 
# mean = 2.0
# std = 3.0
# number of points = 1000
data = np.random.normal(2.0, 3.0, 1000)
plt.hist(data)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

fig = plt.figure()
## Generate gaussian number 
# mean = 2.0
# std = 3.0
# number of points = 1000
##Left plot
img1 = fig.add_subplot(121)
data = np.random.normal(2.0, 3.0, 1000)
plt.hist(data, bins=20, normed=True)
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Histogram')

## right plot
img2 = fig.add_subplot(122)
data = np.random.normal(2.0, 3.0, 1000)
plt.hist(data, bins=20, histtype='step')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()

fig = plt.figure()
## Left plot
img1 = fig.add_subplot(1, 2, 1)
img1.set_xticks([0.1, 0.3, 0.6, 0.9])
img1.set_yticks([0.2, 0.4, 0.5, 0.8])
plt.xlabel('X range')
plt.ylabel('Y range')
plt.title('Numeric ticks')
## Right plot
img2 = fig.add_subplot(1, 2, 2)
img2.set_xticks([0.1, 0.3, 0.6, 0.9])
img2.set_xticklabels(['A','B','C','D'])
img2.set_yticks([0.2, 0.4, 0.5, 0.8])
img2.set_yticklabels(['One','Two','Three','Four'])
plt.xlabel('X range')
plt.ylabel('Y range')
plt.title('Character Ticks')
plt.show()

fig = plt.figure()
img1 = fig.add_subplot(1, 1, 1)
img1.set_xticks([0.1, 0.3, 0.6, 0.9])
img1.set_xticklabels([])
img1.set_yticks([0.2, 0.4, 0.5, 0.8])

# Set the font size 
img1.set_title("Label Plot", fontsize='large', color='blue')

# set properties of font style
for tick in img1.yaxis.get_ticklabels():
    tick.set_fontsize('large')
    tick.set_fontname('Times New Roman')
    tick.set_color('Red')
    tick.set_weight('bold')
plt.show()

fig = plt.figure()
img1 = fig.add_axes([0.1, 0.1, 0.6, 0.8])
N=500
x = np.random.randn(N)
y = np.random.randn(N)
colors = np.random.rand(N)
size =(10 * np.random.rand(N))**2 
scat = img1.scatter(x, y, color=colors, s=size, edgecolor='none')
img1.set_xlim(0., 1.)
img1.set_ylim(0., 1.)
clrbar_img = fig.add_axes([0.7, 0.1, 0.05, 0.8])
fig.colorbar(scat, cax=clrbar_img)
plt.show()

### rcParams are the default parameters for matplotlib
import matplotlib as mpl
plt.rcParams['font.size'] = 11.
plt.rcParams['font.family'] = 'Comic Sans MS'
plt.rcParams['axes.labelsize'] = 15.
plt.rcParams['xtick.labelsize'] = 10.
plt.rcParams['ytick.labelsize'] = 10.

y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]
plt.plot(x1,y, marker='s', linestyle='-', color='y',label='tv')
plt.plot(x2,y, marker='o', linestyle='--', color='g', label='raddio')
plt.xlabel('advertisement medium')
plt.ylabel('Sales')
plt.title('Advertisement effect on sales')
plt.legend(loc='lower right')
plt.show()
