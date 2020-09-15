#!/usr/bin/env pytest-3

import pytest


# Exercice: attributes

class LimitAttributes:
    # TODO
    ...


# test
class FooOnly(LimitAttributes):
    fields = ('foo',)


class BarBazOnly(LimitAttributes):
    fields = ('bar', 'baz')


def test_LimitAttributes():
    f = FooOnly()
    f.foo = 1
    assert f.foo == 1
    with pytest.raises(ValueError):
        f.bar = 2

    b = BarBazOnly()
    b.bar = 1
    assert b.bar == 1
    b.baz = 2
    assert b.baz == 2
    with pytest.raises(ValueError):
        b.foo = 3
