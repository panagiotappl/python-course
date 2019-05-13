from functools import partial, wraps


# Own wraps
def WRAPS(original_fn):  # Arg
    def decorator(proxy_fn):  # Dec
        proxy_fn.__name__ = original_fn.__name__
        proxy_fn.__doc__ = original_fn.__doc__
        proxy_fn.__module__ = original_fn.__module__
        proxy_fn.__qualname__ = original_fn.__qualname__
        return proxy_fn
    return decorator


def inc_result_by(n):  # Arg
    def decorator(fn):  # Dec
        @wraps(fn)
        def proxy(*args, **kwds):  # WrapProx
            return fn(*args, **kwds) + n
        return proxy
    return decorator


def report_result(fn):  # Dec
    @WRAPS(fn)
    def wrapper(*args, **kwds):  # WraProx
        result = fn(*args, **kwds)
        print('result: ', result)
        return result
    return wrapper


def report_args(fn):  # Dec: takes the function being decorated
    @WRAPS(fn)
    def proxy(*args, **kwds):  # WraProx
        print('args: ', args, kwds)
        return fn(*args, **kwds)
    return proxy  # returns the decorated version of the function


@inc_result_by(10)
@report_result
@report_args
def bad(a, b):
    return a * b


print(bad(2, 3))


###################
def eins(_):
    return 1


def inc(n):
    return n+1


def inc_by(n):
    def inc(m):
        return n+m
    return inc


def add(a, b):
    return a+b


class INC_BY:
    def __init__(self, n):
        self.n = n

    def __call__(self, n):
        return self.n + n


@partial(add, 10)
@INC_BY(10)
@inc_by(10)  # 1 + 1 + 10
@inc         # 1 + 1
@eins        # 1
def bonjour():
    return 'hello'


# print(bonjour)

