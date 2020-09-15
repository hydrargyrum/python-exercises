#!/usr/bin/env pytest-3

import pytest


# Exercice: attributes

class Everything42:
    """TODO"""


# test
def test_Everything42():
    e = Everything42()
    assert e.foo == 42
    assert e.bar == 42
    assert e.dsjfidjifdsjifj == 42
    assert e.eioreokriokeokozkkrfkeokokdo == 42
    assert e.fdsidjifjjidsfidjifjdi == 42
    assert e.ezaioepreaprapreuaijre == 42
    assert getattr(e, 'def') == 42
