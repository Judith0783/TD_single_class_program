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
    
"""
Given I add a toy to the toy_list
I want to see the toy in the toy_list
"""
def test_add_new_toy_to_the_toy_list():
    toy_storage = ToyStorage()
    toy_storage.add("teddy")
    
    actual = toy_storage.toy_list
    expected = ["teddy"]
    assert actual == expected 