import sys
import os

class Debug:
    def __init__(self, fn):
        self.fn = fn
        print(sys.platform)
        print(self.fn)

    def __call__(self, arg):
        print(arg)
        print(self.fn(arg))

@Debug
def sample(n):
    if n == 1:
        return n
    else:
        return sample(n-1)

if __name__ == '__main__':
    sample(2)
