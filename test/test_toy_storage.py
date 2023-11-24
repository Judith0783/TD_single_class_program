from lib.toy_storage import *

"""
Given a new instance for ToyStorage
It comes with an empty llist
"""
def test_instantiates_wit_toy_list():
    toy_storage = ToyStorage()
    actual = toy_storage.toy_list
    expected = []
    assert actual == expected # => []