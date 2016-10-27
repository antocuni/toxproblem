import os
import foo

def test_add():
    assert foo.add(1, 2) == 3

def test_PYX():
    use_cython =('USE_CYTHON' in os.environ)
    assert foo.PYX == use_cython
