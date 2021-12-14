def foo(x):
    return bar(x) + 1

def bar(x):
    import os
    os.getenv("HOME", None)
    return x
