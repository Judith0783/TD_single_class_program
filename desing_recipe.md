# Track Tracker Class Desing Recipe


## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have.

As a child
So that i can store my toys 
I want to put toys I've played with to my toy box and see a list of them.

Potential objects:
-ToyStorage
-Toy
-ToyBox

Potential functions/behaviour/features:
- add toys
- see number of toys
- toy list
- toy played with



## 2. Design the Class Interface

Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

class ToyStorage:
    def __init__(self):
        # Properties:
        #   toy_list: list
        # Side effect:
        #    sets toy list to an empty list
        # Return:
        nothing 

    def add_toy(self, toy):
        # Properties:
        # toy: string
        #side effect:
        #   adds toy to the self.toy_list

    def see_toys(self):
        # Properties:
        #   None
        # Side effects:
        #   None (but it returns the self.toy_list)
        # Returns:
        #   returns self.toy_list



## 3. Create Examples as Tests

Make a list of examples of how the class will behave in different situations.

"""
Given a new instance for ToyStorage
It comes with an empty llist
"""
toy_storage = ToyStorage()
actual = toy_storage.toy_list
expected = []
assert actual = expected # => []

"""
Given I add a toy to the toy_list
I want to see the toy in the toy_list
"""
toy_storage = ToyStorage()
toy_storage.add("teddy")
actual = toy_storage.toy_list
expected = ["teddy"]
assert actual == expected # => ["teddy"]

"""
Given I add two toys to the toy_list
I want to see the toys in the toy_list
"""
toy_storage = ToyStorage()
toy_storage.add("teddy")
toy_storage.add("ball")
actual = toy_storage.toy_list
expected = ["teddy" , "ball"]
assert actual == expected # => ["teddy", "ball"]


"""
Given I add some toys to the toy_list
I want to see all toys in the toy_list
"""
toy_storage = ToyStorage()
toy_storage.add("teddy")
toy_storage.add("ball")
toy_storage.add("barbie")

actual = toy_storage.see_toys()
expected = ["teddy" , "ball", "barbie"]
assert actual == expected # => ["teddy", "ball", "barbie"]


## 4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.