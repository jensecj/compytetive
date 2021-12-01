import compytetive as C

# TODO: expect exception on size <= 0 or step <= 0


def test_empty_input_should_output_empty():
    assert list(C.sliding_window([], 1, 1)) == []


def test_misc():
    assert list(C.sliding_window([1, 2, 3], 2, 1)) == [[1, 2], [2, 3]]
    assert list(C.sliding_window([1, 2, 3, 4, 5], 3, 1)) == [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
    ]
    assert list(C.sliding_window([1, 2, 3, 4, 5, 6], 2, 2)) == [
        [1, 2],
        [3, 4],
        [5, 6],
    ]
