from random import randint

vals={"1":1,"5":2,"10":2,"50":2,"1000":4}

sticks=10
iterations=1000
print vals
print len(vals)
for iteration in range(iterations):
    currentSticks=sticks
    while currentSticks>0:
        index=randint(0,len(vals)-1)
        keys=vals.keys()
        val=vals[keys[index]]
        currentSticks -= 1