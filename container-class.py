#!/usr/bin/env pytest-3

import pytest


# Exercice: container

class Range:
    # TODO
    ...


# test
def test_Range():
    big = 100_000_000_000_000
    r = Range(10, big)

    assert len(r) == big - 10

    assert 9 not in r
    assert 10 in r

    for _ in range(1000):  # we must not iterate on r's content
        assert (big - 1) in r
        assert big not in r

    assert r[0] == 10
    assert r[1] == 11

    assert r[len(r) - 1] == big - 1
    assert r[len(r) - 2] == big - 2

    assert r[-1] == big - 1
    assert r[-2] == big - 2

    for bad in (len(r), big, -len(r) - 1):
        with pytest.raises(IndexError):
            r[bad]
