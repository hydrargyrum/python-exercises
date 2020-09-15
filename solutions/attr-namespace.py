#!/usr/bin/env pytest-3

import pytest


# Exercice: attributes

class Namespace:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)


# test
def test_Namespace():
    n = Namespace(baz=1)
    with pytest.raises(AttributeError):
        n.foo
    with pytest.raises(AttributeError):
        n.bar
    assert n.baz == 1

    n = Namespace(foo=2, plop=3)
    assert n.foo == 2
    with pytest.raises(AttributeError):
        n.bar
    with pytest.raises(AttributeError):
        n.baz
    assert n.plop == 3
