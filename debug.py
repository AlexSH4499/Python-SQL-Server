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
