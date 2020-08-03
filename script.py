from inspect import signature as sig
from functools import partial as par

def pipe(value, *args, **kwargs):
    for func in list(args):
        # if len(sig(func).parameters) > 1:
        #     value = func(value)
        # else:
        #     value = func(value)
        value = func(value)

    return value

def add(arg, value):
    return arg / value

(pipe
 (100,
  (par (add, 10)),
  (print)))
