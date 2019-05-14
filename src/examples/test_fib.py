
from pytest import mark
from hypothesis import given, example
from hypothesis.strategies import integers

from fib import fib, fibi

parametrize = mark.parametrize


# @parametrize('fib', (fib, fibi))
# @parametrize('i, o',
#              ((0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13)))
# def test_fib_should_give_correct_results(i, o):
#     assert fib(i) == o
#
#
# @example(10000)
# @given(integers(min_value=2, max_value=1000))
# def test_fib_should_be_sum_of_previous_two(n):
#     assert fib(n) == fib(n-1) + fib(n-2)
