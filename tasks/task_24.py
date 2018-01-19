import re, sys


def isPrime(n):
    # see http://www.noulakaz.net/weblog/2007/03/18/a-regular-expression-to-check-for-prime-numbers/
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None


N = int(12) # number of primes wanted (from command-line) sys.argv[1]
M = 100              # upper-bound of search space
l = list()           # result list

while len(l) < N:
    l += filter(isPrime, range(M - 100, M)) # append prime element of [M - 100, M] to l
    M += 100                                # increment upper-bound

print l[:N] # print result list limited to N elements