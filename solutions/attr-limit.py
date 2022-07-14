#!/usr/bin/env pytest

import pytest


# Exercice: attributes

class LimitAttributes:
    fields = ()

    def __getattr__(self, name):
        if name not in self.fields:
            raise ValueError()
        return super().__getattr__(name)

    def __setattr__(self, name, value):
        if name not in self.fields:
            raise ValueError()
        return super().__setattr__(name, value)

    def __delattr__(self, name):
        if name not in self.fields:
            raise ValueError()
        return super().__delattr__(name)


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
