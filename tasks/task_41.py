a = [(1,),(3,),(4,),(5,),(7,)]
b = [(1,),(2,),(4,),(5,),(8,),(9,)]

def iterate_IDs(set1, set2):
    def next_or_None(seq):
        try:
            return seq.next()
        except StopIteration:
            return None
    id1 = None
    id2 = None
    id1 = next_or_None(set1)
    id2 = next_or_None(set2)
    while id1 is not None or id2 is not None:
        if id1 is None:
            yield (None, id2)
            id2 = next_or_None(set2)
        elif id2 is None:
            yield (id1, None)
            id1 = next_or_None(set2)
        elif id1 == id2:
            yield (id1, id2)
            id1 = next_or_None(set1)
            id2 = next_or_None(set2)
        elif id1 > id2:
            yield (None, id2)
            id2 = next_or_None(set2)
        elif id2 > id1:
            yield (id1, None)
            id1 = next_or_None(set1)
    raise StopIteration, "Both sequences run out"

import itertools as it
for id1,id2 in iterate_IDs(it.chain.from_iterable(a),it.chain.from_iterable(b)):
    print id1, id2
