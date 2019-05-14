from math import sqrt
from hypothesis import given
from hypothesis.strategies import floats

from vector2d import Vector2D

sensible_floats = floats(min_value=0.1, max_value=1e3, allow_nan=False, allow_infinity=False)
FLOATS = sensible_floats



@given(FLOATS, FLOATS)
def test_Vector2D_components_should_be_accessible_as_named_attributes(x, y):
    v = Vector2D(x, y)
    assert v.x == x
    assert v.y == y


@given(FLOATS, FLOATS)
def test_Vector2D_components_should_be_accessible_by_indexing(x, y):
    v = Vector2D(x, y)
    assert v[0] == x
    assert v[1] == y


@given(FLOATS, FLOATS, FLOATS, FLOATS)
def test_Vector2D_attribute_setting_should_work(x, y, new_x, new_y):
    v = Vector2D(x, y)
    v.x = new_x
    assert v.x == new_x
    assert v.y == y
    v.y = new_y
    assert v.y == new_y
    assert v.x == new_x


@given(FLOATS, FLOATS, FLOATS, FLOATS)
def test_Vector2D_setting_via_index_should_work(x, y, new_x, new_y):
    v = Vector2D(x, y)
    v[0] = new_x
    assert v.x == new_x
    assert v.y == y
    v[1] = new_y
    assert v.y == new_y
    assert v.x == new_x


@given(FLOATS, FLOATS, FLOATS, FLOATS)
def test_Vector2D_addition_should_work(x1, y1, x2, y2):
    u = Vector2D(x1, y1)
    v = Vector2D(x2, y2)
    w = u + v
    assert w.x == x1 + x2
    assert w.y == y1 + y2


@given(FLOATS, FLOATS, FLOATS, FLOATS)
def test_Vector2D_subtraction_should_work(x1, y1, x2, y2):
    u = Vector2D(x1, y1)
    v = Vector2D(x2, y2)
    w = u - v
    assert w.x == x1 - x2
    assert w.y == y1 - y2


@given(FLOATS, FLOATS, FLOATS, FLOATS)
def test_Vector2D_in_place_addition_should_work(x1, y1, x2, y2):
    u = Vector2D(x1, y1)
    v = Vector2D(x2, y2)
    u += v
    assert u.x == x1 + x2
    assert u.y == y1 + y2


@given(FLOATS, FLOATS, FLOATS, FLOATS)
def test_Vector2D_in_place_subtraction_should_work(x1, y1, x2, y2):
    u = Vector2D(x1, y1)
    v = Vector2D(x2, y2)
    u -= v
    assert u.x == x1 - x2
    assert u.y == y1 - y2


@given(FLOATS, FLOATS)
def test_Vector2D_unary_minus_should_work(x, y):
    v = Vector2D(x, y)
    w = -v
    assert w.x == -x
    assert w.y == -y


@given(FLOATS, FLOATS, FLOATS)
def test_Vector2D_multiplication_by_scalar_on_left_should_work(x, y, s):
    v = Vector2D(x, y)
    w = s * v
    assert w.x == x * s
    assert w.y == y * s


@given(FLOATS, FLOATS, FLOATS)
def test_Vector2D_multiplication_by_scalar_on_right_should_work(x, y, s):
    v = Vector2D(x, y)
    w = v * s
    assert w.x == x * s
    assert w.y == y * s


@given(FLOATS, FLOATS, FLOATS)
def test_Vector2D_division_by_scalar_should_work(x, y, s):
    s = float(s)
    v = Vector2D(x, y)
    w = v / s
    assert w.x == x / s
    assert w.y == y / s


@given(FLOATS, FLOATS, FLOATS)
def test_Vector2D_in_place_multiplication_by_scalar_should_work(x, y, s):
    v = Vector2D(x, y)
    v *= s
    assert v.x == x * s
    assert v.y == y * s


@given(FLOATS, FLOATS, FLOATS)
def test_Vector2D_in_place_division_by_scalar_should_work(x, y, s):
    s = float(s)
    v = Vector2D(x, y)
    v /= s
    assert v.x == x / s
    assert v.y == y / s


@given(FLOATS, FLOATS)
def test_Vector2D_magnitude_should_work(x, y):
    assert abs(Vector2D(x, y)) == sqrt(x * x + y * y)
