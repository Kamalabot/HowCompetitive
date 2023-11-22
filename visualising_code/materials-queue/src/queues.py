# queues.py
#  

from collections import deque
from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from itertools import count
from typing import Any


class IterableMixin:
    # Creating the Mixin to code the behaviour of the Object
    def __len__(self):
        # Returns the length of the elements
        return len(self._elements)

    def __iter__(self):
        # makes the object iterable
        while len(self) > 0:
            # yields the element, and at the same time deques it
            yield self.dequeue()


class Queue(IterableMixin):
    # Queue Type that extends ItereableMixin for behavior
    def __init__(self, *elements):
        # instantiates double queue with the given collection
        self._elements = deque(elements)

    def enqueue(self, element):
        # adds the element to the end of the quu
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()


class Stack(Queue):
    # inheriting the Queue and overriding the dequeue method for 
    # appending and popping on same side.
    def dequeue(self):
        return self._elements.pop()


class PriorityQueue(IterableMixin):
    # Queue with the priority attached with 
    # each element pushed along with a monotonous counter
    def __init__(self):
        # instantiate with the empty list
        self._elements = []
        # instantiate a counter
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        # priority is negative to make the higher priority to be processed first
        element = (-priority, next(self._counter), value)
        # pushing into the heap to simulate enqueueing
        heappush(self._elements, element)

    def dequeue(self):
        # pop from the heap to simulate dequeueing
        return heappop(self._elements)[-1]


# below data class has rich comparison methods included
@dataclass(order=True)
class Element:
    # Element type that is used inside the queue
    priority: float
    count: int
    value: Any


class MutableMinHeap(IterableMixin):
    def __init__(self):
        super().__init__()
        # instantiating the dictionary for unique values
        self._elements_by_value = {}
        # instantiating the empty elments list
        self._elements = []
        # instantiating the counter
        self._counter = count()

    def __setitem__(self, unique_value, priority):
        # check if unique_value is already in elements_by_value
        if unique_value in self._elements_by_value:
            # yes then assign its priority using the given priority 
            self._elements_by_value[unique_value].priority = priority
            # heapify the elements
            heapify(self._elements)
        else:
            # if not, then create the Element instance
            element = Element(priority, next(self._counter), unique_value)
            # update the element unique_value and element into element by value dictionary
            self._elements_by_value[unique_value] = element
            # push the element into the _elements heap
            heappush(self._elements, element)

    def __getitem__(self, unique_value):
        # locating the item using the unique_value and its priority
        return self._elements_by_value[unique_value].priority

    def dequeue(self):
        # dequeue the element from the heap and returning its value
        return heappop(self._elements).value
