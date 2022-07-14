#!/usr/bin/env pytest

import pytest


# Exercice: comparators

class CaseInsensitiveStr(str):
    def __eq__(self, other):
        return self.lower() == other.lower()

    def __ne__(self, other):
        return self.lower() != other.lower()

    def __lt__(self, other):
        return self.lower() < other.lower()

    def __gt__(self, other):
        return self.lower() > other.lower()

    def __le__(self, other):
        return self.lower() <= other.lower()

    def __ge__(self, other):
        return self.lower() >= other.lower()

    def __hash__(self):
        return hash(self.lower())


# test
def test_CaseInsensitiveStr_cmp():
    cistr = CaseInsensitiveStr

    ufoo = cistr('FOO')
    assert ufoo == 'FOO'
    assert ufoo == 'foo'
    assert ufoo == 'fOO'
    assert ufoo == 'Foo'

    assert str(ufoo) == 'FOO'
    assert str(ufoo) != 'foo'
    assert str(ufoo) != 'Foo'

    assert not (ufoo != 'foo')
    assert not (ufoo != 'fOO')

    assert ufoo > 'faa'
    assert not (str(ufoo) > 'faa')
    assert ufoo >= 'faa'
    assert ufoo < 'fuu'
    assert ufoo <= 'fuu'

    assert sorted(['FUU', 'Foo', 'FOO', 'faa']) == ['FOO', 'FUU', 'Foo', 'faa']
    assert [
        str(cs)
        for cs in sorted([cistr('FUU'), cistr('Foo'), cistr('FOO'), cistr('faa')])
    ] == ['faa', 'Foo', 'FOO', 'FUU']


def test_CaseInsensitiveStr_set():
    cistr = CaseInsensitiveStr

    elems = {cistr('FOO')}
    elems.add(cistr('FOO'))
    assert len(elems) == 1
    assert elems == {cistr('FOO')}
    assert elems == {cistr('Foo')}

    elems.add(cistr('foo'))
    assert len(elems) == 1
    assert elems == {cistr('FOO')}
    assert elems == {cistr('Foo')}

    elems.add(cistr('bar'))
    assert len(elems) == 2
    assert elems == {cistr('FOO'), cistr('bar')}
    assert elems == {cistr('foo'), cistr('BAR')}
