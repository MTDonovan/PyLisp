import operator as op
from functools import partial, reduce


def pipe(value, *args, **kwargs):
    ops = {
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,
        '%': op.mod,
        '^': op.xor
    }
    for expr in list(args):
        if isinstance(expr, tuple) or isinstance(expr, list):
            if expr[0] in ops.keys():
                value = partial(
                    reduce,
                    lambda x, y: ops.get(expr[0])(x, y)
                )([value, *expr[1:]])
            else:
                value = partial(expr[0], value)(*expr[1:])
        else:
            value = expr(value)
    return value


(pipe
 ('TEST',
  (lambda x: x.lower()),
  (print)
 ))


# (pipe
#  (100,
#   ('+', 2, 2, 2),
#   (print)
#  ))
# (print
#  (pipe
#   (100,
#    ('+', 10),
#    (lambda x: x / 2.25))
#  ))
# (pipe
#  (100,
#   ('/', 2),
#   ('+', 100),
#   (print)
#  ))
