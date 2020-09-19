#!/usr/bin/env pytest-3

import bisect
import collections.abc

import pytest


class SortedList(...):
    # TODO
    ...


def test_SortedList():
    lis = SortedList()
    assert list(lis) == []

    lis.add(1)
    assert list(lis) == [1]

    lis.add(5)
    assert list(lis) == [1, 5]

    lis.add(0)
    assert list(lis) == [0, 1, 5]

    lis.add(4)
    assert list(lis) == [0, 1, 4, 5]
    assert(len(lis)) == 4

    assert 0 in lis
    assert 1 in lis
    assert 2 not in lis
    assert 3 not in lis
    assert 4 in lis
    assert 5 in lis

    assert lis[0] == 0
    assert lis[1] == 1
    assert lis[2] == 4
    assert lis[3] == 5
    assert lis[-1] == 5
    assert lis[-2] == 4
    assert lis[-3] == 1
    assert lis[-4] == 0

    with pytest.raises(IndexError):
        lis[4]

    with pytest.raises(IndexError):
        lis[-5]

    lis.add(2)
    assert list(lis) == [0, 1, 2, 4, 5]

    lis.add(3)
    assert list(lis) == [0, 1, 2, 3, 4, 5]

    assert lis.pop(-2) == 4
    assert list(lis) == [0, 1, 2, 3, 5]

    del lis[4]
    assert list(lis) == [0, 1, 2, 3]

    del lis[0]
    assert list(lis) == [1, 2, 3]

    with pytest.raises(IndexError):
        del lis[5]

    with pytest.raises(ValueError):
        lis.remove(0)

    assert list(lis) == [1, 2, 3]
    assert len(lis) == 3

    lis.remove(1)
    assert list(lis) == [2, 3]
