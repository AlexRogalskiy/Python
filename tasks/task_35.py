## Decorator tools

from functools import update_wrapper

# Update wrapper
def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

# Change binary function into n_ary func:

@decorator
def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such that
    f(x, y, z) = f(x, f(y, z)), etc.  Also allow f(x) = x."""
    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args))
    return n_ary_f

# Example of use:
@n_ary
def seq(x, y): return ('seq', x, y)
print seq(1), seq(1, 2), seq(1, 2, 3)

## Memoization
@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be adict key
            return f(args)
    return _f


