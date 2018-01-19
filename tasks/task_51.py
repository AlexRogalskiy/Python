x = 5
print(1 < x < 10)
print(10 < x < 20 )
print(x < 10 < x*10 < 100)
print(10 > x <= 9)
print(5 == x > 4)

odds = (n for n in range(1,10) if n % 2)
for n in odds:
    print n

a = ['a', 'b', 'c', 'd', 'e']
for index, item in enumerate(a): print index, item

def mygen():
    a = 5
    while True:
        f = (yield a) # yield a and possibly get f in return
        if f is not None: 
            a = f  # store the new value
			
g = mygen()
print g.next()
print g.next()
print g.send(7)  # we send this back to the generator
print g.next() # now it will yield 7 until we send something else

a = [1,2,3,4,5]
print a[::2]  # iterate over the whole list in 2-increments
print a[::-1] # a useful idiom for 'x reversed'

from random import randrange
n = 5
foo = [randrange(10) for i in range(n)]

for i in foo:
    if i == 0:
        print('found 1')
else:
    print('did not find 1')

def draw_point(x, y):
    print (x, y)
point_foo = (3, 4)
point_bar = {'y': 3, 'x': 2}
draw_point(*point_foo)
draw_point(**point_bar)

