import itertools

flatten = lambda x: list(itertools.chain.from_iterable(x))

s = [['"', 'An', 'investment'], ['in'], ['knowledge'], ['pays'], ['the', 'best'], ['interest."', '--'], ['Benjamin'], ['Franklin']]
print(' '.join(flatten(s)))
