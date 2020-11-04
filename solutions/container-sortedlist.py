#!/usr/bin/env pytest-3

import bisect
import collections.abc

import pytest


class SortedList(collections.abc.Sequence):
    # Subclassing `list` is possible but discouraged because it would still expose
    # the `append` and `insert` methods, which can make the list unsorted.
    def __init__(self, iterable=()):
        self.data = sorted(iterable)

    # internal methods
    def _find_lt(self, v):
        return bisect.bisect_left(self.data, v)

    def _find_rt(self, v):
        return bisect.bisect_right(self.data, v)

    def _find(self, v):
        pos = bisect.bisect_left(self.data, v)
        if pos < len(self) and self[pos] == v:
            return pos
        return -1

    # Sequence interface
    def __contains__(self, v):
        return self._find(v) >= 0

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, k):
        return self.data[k]

    def add(self, v):
        bisect.insort_left(self.data, v)

    # 'list' interface
    def __delitem__(self, k):
        del self.data[k]

    def remove(self, v):
        pos = self._find(v)
        if pos < 0:
            raise ValueError('%r not in SortedList' % v)
        else:
            del self[pos]

    def extend(self, iterable):
        for v in iterable:
            self.add(v)

    def append(self, v):
        raise TypeError('cannot append values in SortedList')

    def index(self, v):
        pos = self._find(v)
        if pos < 0:
            raise ValueError('%r not in SortedList' % v)
        return pos

    def count(self, v):
        pos = self._find_lt(v)
        count = 0
        for pos in range(pos, len(self)):
            if self[pos] != v:
                break
            count += 1
        return count

    def pop(self, index=-1):
        return self.data.pop(index)

    def clear(self):
        self.data.clear()


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
