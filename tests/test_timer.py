# A context manager for timing code. Note: do not use this for serious
# timings: the overhead will be too large when the timed duration is
# very short. For serious timings use the timeit module.
from contextlib import contextmanager

from pytest import mark
from time import sleep, time


class T:
    def __init__(self):
        self.time = 0


@contextmanager
def timer():
    start_time = time()
    t = T()
    yield t
    t.time = time() - start_time


@mark.parametrize('seconds_to_sleep', range(1,4))
def test_timer_should_report_approximately_correct_times(seconds_to_sleep):
    with timer() as t:
        sleep(seconds_to_sleep)
    sleep(1)
    assert abs(t.time - seconds_to_sleep) < 0.01
