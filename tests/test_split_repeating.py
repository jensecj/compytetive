import random
import compytetive as C


def test_empty_input_should_output_empty():
    assert C.split_repeating("") == []
    assert C.split_repeating([]) == []


def test_single_input_should_output_that():
    assert C.split_repeating("a") == [["a"]]
    assert C.split_repeating(["a"]) == [["a"]]
    assert C.split_repeating([1]) == [[1]]


def test_misc():
    assert C.split_repeating("bba") == [["b", "b"], ["a"]]
    assert C.split_repeating("abb") == [["a"], ["b", "b"]]
    assert C.split_repeating("abbccc") == [["a"], ["b", "b"], ["c", "c", "c"]]
