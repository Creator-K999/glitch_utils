import trace

def AutoLog(func):
    def wrapper(*args, **kwargs):
        tracer = trace.Trace(count=False, trace=True)
        tracer.runfunc(func, *args, **kwargs)

    return wrapper

def two():
    return 5

@AutoLog
def myFunc():
    x = 15
    x *= 16
    print(x)
    two()
    x /= 0

myFunc()
