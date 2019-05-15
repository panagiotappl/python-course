# Test-Drivenly-Develop code to satisfy the following requirements.
#
# 1. A class called Window should be constructable by specifying the position of the lower left corner of the window
# along with its width and height
# 2. Instances of Window should have attributes x, y, width, height. x and y should indicate the centre of the
# rectangle.
# 3. x and y should be read-only.
# 4. The class should have an area() method which returns the area of the window.
# 5. It should have a perimeter() method which returns the perimeter of the window.
# 6. It should be possible to construct instances of Window by specifying the (x,y) coordinates of two of its corners.
# 7. It should have a subclass called BorderWindow, which is just like Window, except that the area and perimeter
# methods take into account the implicit presence of a border of thickness 5 units, in excess of the dimensions
# specified during construction.
from pytest import raises

from src.window import Window, BorderWindow


def test_construct_window_from_lower_left_corner_and_width_height():
    w = Window((10, 20), (50, 60))
    assert type(w) is Window
    assert w.x == 35
    assert w.y == 50
    assert w.width == 50
    assert w.height == 60


# Should be one test for x and one for y
def test_x_and_y_should_be_read_only():
    w = Window((11, 21), (52, 62))

    with raises(AttributeError):
        w.x = 0

    with raises(AttributeError):
        w.y = 0


def test_area():
    w = Window((12, 22), (54, 64))
    assert w.area() == 3456


def test_perimeter():
    w = Window((13, 23), (56, 66))
    assert w.perimeter() == 244


def test_constructor_from_corners():
    w = Window.from_corners((100, 200), (600, 400))
    assert w.x == 350
    assert w.y == 300
    assert w.width == 500
    assert w.height == 200


def test_border_window_area_main_contructor():
    w = BorderWindow((10, 20), (50, 60))
    assert type(w) is BorderWindow
    assert w.x == 35
    assert w.y == 50
    assert w.width == 60
    assert w.height == 70


def test_bordered_area():
    w = BorderWindow((12, 22), (54, 64))
    assert w.area() == 6216

def test_construct_from_corners_border_window():
    w = BorderWindow.from_corners((100, 200), (600, 400))
    assert w.x == 350
    assert w.y == 300
    assert w.width == 510
    assert w.height == 210
