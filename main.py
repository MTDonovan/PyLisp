import operator as op
from functools import partial, reduce


def thread(value, *args, **kwargs):
    '''
    The "thread" function is a basic implementation of the threading macro from Lisp.
    '''
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
