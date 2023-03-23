import pytest


def always_returns_true():
    # it should have been True
    y = 100 + 20
    return y


def test_always_returns_true():

    
    # No changes here
    assert always_returns_true()
 