import random
import compytetive as C


def test_empty_input_should_output_zero():
    assert C.most_repeating_element("") == (None, 0)
    assert C.most_repeating_element([]) == (None, 0)


def test_single_input_should_output_one():
    assert C.most_repeating_element("a") == ("a", 1)
    assert C.most_repeating_element(["a"]) == ("a", 1)
    assert C.most_repeating_element([1]) == (1, 1)


def test_misc():
    assert C.most_repeating_element("aa") == ("a", 2)
    assert C.most_repeating_element(["a", "a"]) == ("a", 2)
    assert C.most_repeating_element("abbbcccc") == ("c", 4)
    assert C.most_repeating_element(["a", "b", "c", "c", "c"]) == ("c", 3)
    assert C.most_repeating_element([1, 1, 1, 3, 4, 5, 6, 6, 6, 6, 7]) == (6, 4)


def test_fuzz():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for _ in range(1000):
        i = random.randint(2, 100)
        p = random.randint(0, len(alpha) - 1)
        t = alpha[:p] + (i * alpha[p]) + alpha[p:]
        assert C.most_repeating_element(t) == (alpha[p], i + 1)
