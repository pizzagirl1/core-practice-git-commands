import pytest


def always_returns_true():
    # this time i added a comment
    x = None
    return x 


def test_always_returns_true():
    assert always_returns_true()
