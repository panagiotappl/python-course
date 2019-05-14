from pytest import mark


def fn(a, b):
    return a + b


@mark.parametrize("a, b, c",
                 [(0, 0, 0),
                 (-1, 0, -1),
                 (0, -1, -1)])
def test_fn(a, b, c):
    assert fn(a, b) == c
