from array import *

q = [1,2,3,4,5]
t = [s for s in q if s > 3]
w = map(lambda q: q,filter(lambda d:d>2, q))
#print t, w

p = []
for i in range(5):
	p.append([x for x in range(6)])
    
#print p

def add_letters(l):
	for y in l:
		yield y

hash = {'help' : ['h','e','l','p']}

h = add_letters(hash['help'])
print ''.join(hash['help'])
print ''.join([d for d in h])

class Mega(object):
	
    def __init__(self, name):
		print 'Setting up the Mega object'
		self.name = name
    def __str__(self):
		return self.name
        
m = Mega('Arkadiusz')
print str(m)

def cheat_args(function):
    def wrapper(*args, **kwargs):
        if len(args[0]) > 0:
            args[0][0] = 'It\'s sneaky'
        return function(*args, **kwargs)
    return wrapper
    
@cheat_args    
def writy(to_write):
    print to_write
    for i in to_write:
        print i
        
#writy(['One', 'Two', 'Three'])

life = [[0 for i in range(4)] for i in range(4)]
print life [1][1]


    

