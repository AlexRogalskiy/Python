class count_iterator(object):
    n = 0

    def __iter__(self):
        return self

    def next(self):
        y = self.n
        self.n += 1
        return y

counter = count_iterator()

class SimpleList(object):
    def __init__(self, *items):
        self.items = items

    def __getitem__(self, i):
        return self.items[i]

a = SimpleList(1, 2, 3)
it = iter(a)
next(it)

class qsequence(object):
    def __init__(self, s):
        self.s = s[:]

    def next(self):
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self

    def current_state(self):
        return self.s
Q = qsequence([1, 1])
[next(Q) for __ in xrange(10)]



def collatz(n):
   yield n
   while n != 1:
     n = n / 2 if n % 2 == 0 else 3 * n + 1
     yield n
list(collatz(7))


def tent_map(mu, x0):
    x = x0
    while True:
        yield x
        x = mu * min(x, 1.0 - x)


t = tent_map(2.0, 0.1)
for __ in xrange(30):
	print t.next()



import random
def bernoulli_process(p):
    if p > 1.0 or p < 0.0:
        raise ValueError("p should be between 0.0 and 1.0.")

    while True:
        yield random.random() < p


def von_neumann_extractor(process):
    while True:
        x, y = process.next(), process.next()
        if x != y:
            yield x

def hofstadter_generator(s):
    a = s[:]
    while True:
        try:
            q = a[-a[-1]] + a[-a[-2]]
            a.append(q)
            yield q
        except IndexError:
            return



def permutations(items):
    if len(items) == 0:
        yield []
    else:
        pi = items[:]
        for i in xrange(len(pi)):
            pi[0], pi[i] = pi[i], pi[0]
            for p in permutations(pi[1:]):
                yield [pi[0]] + p

for p in permutations([1, 2, 3]):
	print p


g = (x ** 2 for x in itertools.count(1))
next(g)
iter(g) is g
[g.next() for __ in xrange(10)]


g = (random.random() < 0.4 for __ in itertools.count())
[g.next() for __ in xrange(10)]


sum(x ** 2 for x in xrange(10))


from itertools import combinations, product
n = 4
d = 3
def visit(*indices):
    print indices
# Loop through all possible indices of a 3-D array
for i in xrange(n):
    for j in xrange(n):
        for k in xrange(n):
            visit(i, j, k)

# Equivalent using itertools.product
for indices in product(*([xrange(n)] * d)):
    visit(*indices)

# Now loop through all indices 0 <= i < j < k <= n
for i in xrange(n):
    for j in xrange(i + 1, n):
        for k in xrange(j + 1, n):
            visit(i, j, k)

# And equivalent using itertools.combinations
for indices in combinations(xrange(n), d):
    visit(*indices)


import itertools
import math
def inversion_number(A):
    """Return the number of inversions in list A."""
    return sum(1 for x, y in itertools.combinations(xrange(len(A)), 2) if A[x] > A[y])
def total_inversions(n):
    """Return total number of inversions in permutations of n."""
    return sum(inversion_number(A) for A in itertools.permutations(xrange(n)))
[total_inversions(n) for n in xrange(10)]
[math.factorial(n) * n * (n - 1) / 4 for n in xrange(10)]


def count_fixed_points(p):
    """Return the number of fixed points of p as a permutation."""
    return sum(1 for x in p if p[x] == x)

def count_partial_derangements(n, k):
    """Returns the number of permutations of n with k fixed points."""
    return sum(1 for p in itertools.permutations(xrange(n)) if count_fixed_points(p) == k)
[count_partial_derangements(6, i) for i in xrange(7)]
