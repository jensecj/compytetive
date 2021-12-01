import random
import compytetive as C


def test_empty_input_should_output_empty():
    assert C.manhatten_dist((0, 0), (0, 0)) == 0
