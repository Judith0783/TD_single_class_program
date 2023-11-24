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
    
"""
Given I add two toys to the toy_list
I want to see the toys in the toy_list
"""
def test_add_new_two_toys_to_the_toy_list():
    toy_storage = ToyStorage()
    toy_storage.add("teddy")
    toy_storage.add("ball")
    
    actual = toy_storage.toy_list
    expected = ["teddy" , "ball"]
    assert actual == expected 
    
"""
Given I add some toys to the toy_list
I want to see all toys in the toy_list
"""
def test_see_all_toys():
    toy_storage = ToyStorage()
    toy_storage.add("teddy")
    toy_storage.add("ball")
    toy_storage.add("barbie")

    actual = toy_storage.see_toys()
    expected = ["teddy" , "ball", "barbie"]
    assert actual == expected # => ["teddy", "ball", "barbie"]

