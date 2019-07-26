class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
         
        if self.current >= self.capacity:
          self.current = 0
 
        self.storage[self.current] = item
        self.current += 1

        # return self.storage

    def get(self):
        getStorage = []

        for i in range(self.capacity):
            if self.storage[i] != None:
                getStorage.append(self.storage[i])

        return getStorage


        


"""
Test in Terminal:
cd in folder
$ python3
from ring_buffer import RingBuffer
temp = RingBuffer(3)
temp.get()
temp.append("A")
temp.append("B")
temp.get()
temp.append("EE")
temp.get()
"""


""" 
Append() Plan - First Round:

- self.storage initialized at 0
- set item to self.storage at index equal self.current 
- after each append, if self.current < self.capacity, increment self.current + 1 to move to next index in array
- or if once self.current == self.capacity - 1 (accounting for index 0), reset self.current to 0 instead of incrementing

- REFACTOR & CLEAN -- Is there repeating code? How can we optimize this to not repeat code?

"""

"""
Get() Plan:

- empty array
- iterate through self.storage
- append value at index i to new array if value != None
- return the new array
"""