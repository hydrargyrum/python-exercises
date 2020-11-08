#!/usr/bin/env pytest-3

from weakref import ref
from argparse import Namespace as N

import pytest


# Exercice: weak references

class Store:
    # TODO
    ...


# test
def test_weakrefs():
    store = Store()

    first = N(value=1)
    store['first object'] = first

    assert store['first object'].value == 1
    assert store['first object'] is first
    with pytest.raises(KeyError):
        store['another']
    with pytest.raises(KeyError):
        store['nope']

    second = N(value=2)
    store['another'] = second
    assert store['first object'] is first
    assert store['another'].value == 2
    assert store['another'] is second
    with pytest.raises(KeyError):
        store['nope']

    del first
    with pytest.raises(KeyError):
        store['first object']
    with pytest.raises(KeyError):
        store['nope']
