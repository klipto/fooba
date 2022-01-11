import point
import unittest

class MyTest(unittest.TestCase):
    def test_method1(self):
        assert point.foo(10) == 11
        
def test_foo():
    assert point.foo(10) == 11

def test_spurious_function():
    assert point.spurious_function(10) == 1
