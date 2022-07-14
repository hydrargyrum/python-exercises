#!/usr/bin/env pytest

import pytest


# Exercice: decorators

def accept_only_multiples_of(param):
    # TODO
    ...


# test
def test_accept_only_multiples_of():
    @accept_only_multiples_of(2)
    def filtered_2(n):
        return n + 1

    def base(n):
        return n + 1

    filtered_3 = accept_only_multiples_of(3)(base)
    filtered_5 = accept_only_multiples_of(5)(base)

    assert filtered_2(0) == 1
    assert filtered_2(2) == 3
    assert filtered_2(4) == 5

    for bad in (1, 3, 5):
        with pytest.raises(ValueError):
            filtered_2(bad)

    assert filtered_3(0) == 1
    assert filtered_3(3) == 4
    assert filtered_3(6) == 7

    for bad in (1, 2, 4, 5, 7, 8):
        with pytest.raises(ValueError):
            filtered_3(bad)

    assert filtered_5(0) == 1
    assert filtered_5(5) == 6
    assert filtered_5(10) == 11

    for bad in (1, 2, 3, 4, 6, 7, 8, 9, 11):
        with pytest.raises(ValueError):
            filtered_5(bad)
