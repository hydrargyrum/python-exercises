#!/usr/bin/env pytest-3

from functools import wraps

import pytest


# Exercice: decorators

def accept_only_even(decorated):
    @wraps(decorated)  # optional, but best practise: copies documentation etc.
    def wrapper(n):
        if n % 2:
            raise ValueError()
        return decorated(n)

    return wrapper


# test
def test_accept_only_even():
    @accept_only_even
    def same(n):
        return n

    @accept_only_even
    def add_1(n):
        return n + 1

    assert same(0) == 0
    assert add_1(0) == 1

    assert same(2) == 2
    assert add_1(2) == 3

    assert same(42) == 42
    assert add_1(42) == 43

    for bad in (1, 3, 41):
        with pytest.raises(ValueError):
            same(1)
        with pytest.raises(ValueError):
            add_1(1)
