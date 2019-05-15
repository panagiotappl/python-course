from math import sqrt
from contextlib import contextmanager

from pytest import raises

# class my_raises:
#
#     def __init__(self, exception):
#         self._exception = exception
#
#     def __enter__(self):
#         pass
#
#     def __exit__(self, exception_type, exception_value, traceback):
#         if exception_type == self._exception
#             assert True
#         else:
#             assert False


@contextmanager
def my_raises(exception):
    try:
        yield
    except exception:
        assert True
    except:
        assert False
    else:
        assert False


def test_sqrt_should_raise_ValueError_on_negative_input_using_pytest_raises():
    with my_raises(ValueError):
        sqrt(-1)


# deprecated
# def test_sqrt_should_raise_ValueError_on_negative_input_using_pytest_raises_bad():
#     raises(ValueError, 'sqrt(-1)')


def test_sqrt_should_raise_ValueError_on_negative_input_using_pytest_raises_ugly():
    raises(ValueError, lambda: sqrt(-1))
    # pythonic way
    # raises(ValueError, sqrt, -1)

