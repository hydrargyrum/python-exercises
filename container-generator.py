#!/usr/bin/env pytest

import pytest


# Exercice: iter

def multiples_of(n):
    # TODO
    ...


# test
def test_iter():
    gen = multiples_of(3)
    for n, mult in enumerate(gen):
        assert n * 3 == mult
        if n >= 100:
            break

    for n, mult in enumerate(gen):
        assert (n + 101) * 3 == mult
        if n >= 100:
            break

    gen = multiples_of(4)
    for n, mult in enumerate(gen):
        assert n * 4 == mult
        if n >= 100:
            break
