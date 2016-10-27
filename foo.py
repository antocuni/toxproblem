try:
    import cython
except ImportError:
    PYX = False
else:
    PYX = cython.compiled


def add(x, y):
    return x+y
