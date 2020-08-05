from functools import partial, reduce
# from inspect import signature as sig


def thread(value, *args, **kwargs):
    for expr in list(args):
        if isinstance(expr, tuple) or isinstance(expr, list):
            if expr[0] in ("+", "-", "*", "/"):
                value = partial(reduce, lambda x, y: eval("{0} {1} {2}".format(x, expr[0], y)))([value, *expr[1:]])
            else:
                value = partial(expr[0], value)(*expr[1:])
        else:
            value = expr(value)
    return value


(thread
 (100,
  ('+', 2, 2, 2),
  (print)))

(print
 (thread
  (100,
   ('+', 10),
   (lambda x: x / 2))))
