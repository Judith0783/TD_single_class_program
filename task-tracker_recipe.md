# Track Tracker Class Desing Recipe


## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

class TaskTracker():
    def add(self, task):
        # Parameters:
        #   task: string, representing a task
    pass

    def list_incomplete(self):
        #  returns:
        #   A list of incomplete task
        pass

    def _mark_complete():
        #   Parameters:
        #       Index: An integer representing the task to complete
        #   Side effect:
        #       Removes the task at index from the list of tasks
        pass




## 3. Create Examples as Tests

Make a list of examples of how the class will behave in different situations.

"""
Initially there are not tasks
"""
tracker = TaskTracker()
tracker.list_incomplete() # => []

"""
When we add a task
It is reflected in the list of task
"""
tracker = TaskTracker()
tracker.add("walk the dog")
tracker.list_incomplete() # => ["Walk the dog"]

"""
When we add a multiple tasks
They are all reflected in the list of tasks
"""
tracker = TaskTracker()
tracker.add("walk the dog")
tracker.add("walk the cat")
tracker.add("walk the frog")
tracker.list_incomplete() # => ["Walk the dog", "walk the cat", "walk the frog" ]

"""
When we add a multiple tasks
And mark one as complete
It disappears from the task list
"""
tracker = TaskTracker()
tracker.add("walk the dog")
tracker.add("walk the cat")
tracker.add("walk the frog")
tracker.mark_complete(1)
tracker.list_incomplete() # => ["Walk the dog", "walk the frog" ]

"""
If we try to mark a track complete that does not exist (too low)
It raises an error
"""
tracker = TaskTracker()
tracker.add("walk the dog")
tracker.mark_complete(-1) # Raises an error "No such a task to mark complete" 
tracker.list_incomplete() # => ["Walk the dog"]

If we try to mark a track complete that does not exist (too high)
It raises an error
"""
tracker = TaskTracker()
tracker.add("walk the dog")
tracker.mark_complete(2) # Raises an error "No such a task to mark complete"
tracker.list_incomplete() # => ["Walk the dog"]


# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
Encode each example as a test. You can add to the above list as you go.

## 4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.