#!/usr/bin/env pytest

from contextlib import contextmanager

import pytest


# Exercice: context manager

@contextmanager
def stack_context(lis):
    lis.append(len(lis))
    try:
        yield
    finally:
        lis.pop(-1)


# test
def test_stack_context():
    lis = []
    with stack_context(lis):
        assert lis == [0]
        with stack_context(lis):
            assert lis == [0, 1]
        assert lis == [0]
    assert lis == []


def test_stack_context_error():
    lis = []
    with pytest.raises(ZeroDivisionError):
        with stack_context(lis):
            assert lis == [0]
            with stack_context(lis):
                assert lis == [0, 1]
                1 / 0  # it's ok
    assert lis == []

