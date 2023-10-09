from trace import Trace
from importlib import import_module
from os.path import dirname
from inspect import getmodule

__DEBUG = True


class AutoLogD:
        def __init__(self, to_ignore_dir):
            self.to_ignore_dir = to_ignore_dir

        def __call__(self, func):
            def wrapper(*args, **kwargs):
                tracer = Trace(count=False, trace=True, ignoredirs=self.to_ignore_dir)
                tracer.runfunc(func, *args, **kwargs)

            return wrapper
        

class AutoLogR:
        def __call__(self, func):
            return func


def auto_log_factory(to_ignore_dir: list[str] = []):
    if __DEBUG:
        if to_ignore_dir:
            modules = [getmodule(import_module(x)) for x in to_ignore_dir]

            if modules:
                return AutoLogD([dirname(x.__file__) for x in modules if x]) # type: ignore
        else:
            return AutoLogD([])
    
    else:
        return AutoLogR()


def set_flags(debug: bool):
   
   global __DEBUG

   __DEBUG = debug
