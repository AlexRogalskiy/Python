def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a+b

f = fib()
for x in xrange(10):
    print f.next(),