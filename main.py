import pytest


def always_returns_true():
    # it should have been True
    frogs = True
    if frogs:
        return True
    else:
        return False


def test_always_returns_true():

    
    # No changes here
    assert always_returns_true()