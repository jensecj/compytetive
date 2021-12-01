import compytetive as C


def test():
    assert C.chinese_remainder([3, 5, 7], [2, 3, 2]) == 23
    assert C.chinese_remainder([5, 7, 9, 11], [1, 2, 3, 4]) == 1731
    assert C.chinese_remainder([11, 12, 13], [10, 4, 12]) == 1000


def test_none():
    assert not C.chinese_remainder([2, 3, 2], [7, 1005, 15])
    assert not C.chinese_remainder([11, 22, 19], [10, 4, 9])
