import math
import compytetive as C


def test_center_rotating_around_self_should_not_move():
    assert C.rotate_point((0, 0), (0, 0), 90) == (0, 0)


def test_misc():
    x, y = C.rotate_point((10, 1), (0, 0), 90)
    assert math.isclose(x, 1) and math.isclose(y, -10)
