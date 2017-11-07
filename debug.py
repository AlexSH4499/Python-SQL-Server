from functools import wraps
from time import time

def timer(fn):
    @wraps(fn)
    def wrap(*args, **kw):
        time_start = time()
        result = fn(*args,**kw)
        time_end = time()
        print('function:{}\took:{} \n args:{} \n kwargs:{}'\
              .format(fn.__name__,time_end-time_start,args,kw))
        return result
    return wrap
