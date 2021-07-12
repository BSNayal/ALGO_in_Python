#Stack using python list
import random

class Stack(object):
    def __init__(self):
        self._stack = []

    def push(self, value):
        print("PUSHING {} ON THE STACK".format(value))
        self._stack.append(value)

    def pop(self):
        print("POPPING NUMBER FROM STACK")
        if self._stack:
            return self._stack.pop()
        else:
            print("STACK IS EMPTY")
    
    def top(self):
        print("TOP NUMBER ON THE STACK")
        if self._stack:
            return self._stack[-1]
        else:
            print("STACK IS EMPTY")

    def display(self):
        print("PRINTING THE STACK")
        for i, val in enumerate(self._stack[::-1]):
            print(val)
            if i != len(self._stack) - 1:
                print("|")
                
            


obj = Stack()

for i in range(10):
    obj.push(random.randint(1, 100))
obj.display()
obj.pop()
obj.display()
obj.push(112)
obj.display()
obj.pop()
obj.display()
obj.pop()
obj.display()
print(obj.top())
print("\n")