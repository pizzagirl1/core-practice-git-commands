import pytest


def always_returns_true():
    # it should have been True
    y = True
    return y


def test_always_returns_true():

    
    # No changes here
    assert always_returns_true()
 