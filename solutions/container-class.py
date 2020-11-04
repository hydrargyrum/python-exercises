#!/usr/bin/env pytest-3

import pytest


# Exercice: container

class Range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        n = self.start
        while n < self.stop:
            yield n
            n += 1

    def __len__(self):
        return self.stop - self.start

    def __getitem__(self, n):
        if n >= len(self) or n < -len(self):
            raise IndexError()
        elif n >= 0:
            return self.start + n
        else:
            return self.stop + n

    def __contains__(self, n):
        return self.start <= n < self.stop


# test

BIG = 100_000_000_000_000


def test_len():
    r = Range(10, BIG)

    assert len(r) == BIG - 10


def test_iter():
    r = Range(10, BIG)

    for n, value in enumerate(r):
        assert value == n + 10
        if n > 10:
            break


def test_contains():
    r = Range(10, BIG)

    assert 9 not in r
    assert 10 in r

    for _ in range(1000):  # we must not iterate on r's content
        assert (BIG - 1) in r
        assert BIG not in r


def test_random_access():
    r = Range(10, BIG)

    assert r[0] == 10
    assert r[1] == 11

    assert r[len(r) - 1] == BIG - 1
    assert r[len(r) - 2] == BIG - 2

    assert r[-1] == BIG - 1
    assert r[-2] == BIG - 2

    for bad in (len(r), BIG, -len(r) - 1):
        with pytest.raises(IndexError):
            r[bad]
