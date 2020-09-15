#!/usr/bin/env pytest-3

import pytest


# Exercice: try..except

class ExBase:
    normal_called = False
    error_called = False
    always_called = False

    def normal(self):
        self.normal_called = True

    def error(self):
        self.error_called = True

    def always(self):
        self.always_called = True


class ExYour(ExBase):
    def question(self):
        # TODO
        ...


# test
def test_ExYour():
    class Norm(ExYour):
        pass

    n = Norm()
    n.question()
    assert n.normal_called
    assert not n.error_called
    assert n.always_called

    class Failed(ExYour):
        def normal(self):
            self.normal_called = True
            raise Exception()

    f = Failed()
    f.question()
    assert f.normal_called
    assert f.error_called
    assert f.always_called
