from nose.tools import *
import depopwatch

@raises(AssertionError)
def test_no_username():
    depopwatch.Listener(None)

@raises(AssertionError)
def test_nonexistent_username():
    #This account seems to be reserved and in a state of non-existance
    depopwatch.Listener("a")
