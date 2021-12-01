import math
import itertools as it
import functools as ft
import operator as op

from collections import deque

from typing import Any, Tuple, Generator

Point = Tuple[int, int]


def most_repeating_element(coll: list[Any]) -> Tuple[Any, int]:
    """
    Return the element which occurs in the longest repeating subset of COLL,
    and the length of that subset.
    """
    if len(coll) == 1:
        return coll[0], 1

    longest = 0
    current = 1
    last = None
    element = None

    for e in coll:
        if last == e:
            element = e
            current += 1
            longest = max(current, longest)
        else:
            current = 1

        last = e

    return element, longest


def split_repeating(coll: list[Any]) -> list[Any]:
    """Split collection whenever """
    return [list(y) for x, y in it.groupby(coll)]


def flatten(coll: list[Any]) -> list[Any]:
    """Flatten a nested list into a single list."""
    flat = []
    to_flatten = deque(coll)
    while to_flatten:
        e = to_flatten.popleft()
        if isinstance(e, list):
            to_flatten.extendleft(reversed(e))
        else:
            flat.append(e)

    return flat


def sliding_window(coll: list[Any], size: int, step: int = 1) -> Generator[list[Any], None, None]:
    """Return sliding views of COLL, of size SIZE, and moving STEP steps each iteration."""
    assert size > 0
    assert step > 0

    d = deque(coll[:size])

    i = size
    end = len(coll)
    while i <= end:
        yield list(d)

        for _ in range(step):
            d.popleft()

        for e in coll[i : i + step]:
            d.append(e)

        i += step


def manhatten_dist(a: Point, b: Point):
    """Return the Manhatten Distance between points A and B."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def rotate_point(point: Point, center: Point, degrees: int):
    """Rotate POINT around CENTER by DEGREES"""
    px, py = point
    cx, cy = center
    r = -math.radians(degrees)

    x = math.cos(r) * (px - cx) - math.sin(r) * (py - cy) + cx
    y = math.sin(r) * (px - cx) + math.cos(r) * (py - cy) + cy
    return (x, y)


def chinese_remainder(moduli, residues):
    """Return the unique remainder"""
    try:
        total = 0
        N = ft.reduce(op.mul, moduli)

        for m, r in zip(moduli, residues):
            p = N // m
            total += r * pow(p, -1, m) * p

        return total % N
    except ValueError:
        return None
