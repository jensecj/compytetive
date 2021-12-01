import random
import compytetive as C


def test_empty_input_should_output_empty():
    assert C.flatten([]) == []


def test_single_input_should_output_that():
    assert C.flatten(["a"]) == ["a"]
    assert C.flatten([1]) == [1]


def test_nested_list_should_flatten():
    assert C.flatten([[1]]) == [1]
    assert C.flatten([[[["a"]]]]) == ["a"]


def test_misc():
    assert C.flatten([[1], [2, 3], [4], [5, [6]]]) == [1, 2, 3, 4, 5, 6]
    assert C.flatten([[["1"], 2], [3, 4], [[["5"]]]]) == ["1", 2, 3, 4, "5"]
