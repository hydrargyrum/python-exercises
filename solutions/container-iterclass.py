#!/usr/bin/env pytest-3

import pytest


# Exercice: iter

class MultiplesOf:
    def __init__(self, factor):
        self.factor = factor

    def __iter__(self):
        n = 0
        while True:
            yield n
            n += self.factor


# test
def test_iter():
    gen = MultiplesOf(3)
    for n, mult in enumerate(gen):
        assert n * 3 == mult
        if n >= 100:
            break

    for n, mult in enumerate(gen):
        assert n * 3 == mult
        if n >= 100:
            break

    gen = MultiplesOf(4)
    for n, mult in enumerate(gen):
        assert n * 4 == mult
        if n >= 100:
            break
