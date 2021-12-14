class T:
    def __init__(self, x):
        self.x = x
    def baz(self, x):
        import os
        os.getenv("HOME", None)
        return x + self.x
    
def foo(x):
    return bar(x) + 1

def bar(x):
    return T(0).baz(x)
