import operator as op
from functools import partial, reduce


def thread(value, *args, **kwargs):
    '''
    The "thread" function is a basic implementation of the threading
    macro from Lisp.
    Using the "operator" library, developers can execute "Reverse Polish
    notation (RPN)" functions within the context of a "thread" function.
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

(thread
 ('TEST',
  (lambda x: x.lower()),
  (print)))

(thread
 (100,
  ('+', 2, 2, 2),
  (print)))

(print
 (thread
  (100,
   ('+', 10),
   (lambda x: x / 2.25))))

(thread
 (100,
  ('/', 2),
  ('+', 100),
  (print)))
