from inspect import signature as sig
from functools import partial


# if len(sig(func).parameters) > 1:
#     value = func(value)
# else:
#     value = func(value)

def pipe(value, *args, **kwargs):
    for expr in list(args):
        if isinstance(expr, tuple) or isinstance(expr, list):
            value = partial(*expr)(value)
        else:
            value = expr(value)
    return value

def add(*args):
    from functools import reduce
    return reduce(lambda x, y: x + y, list(args))

(pipe
 (100,
  (add, 10, 20, 30),
  (print)))

(print
 (pipe
  (100,
   (add, 10),
   (lambda x: x / 2))))
