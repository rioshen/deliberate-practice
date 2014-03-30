#!/usr/bin/env python

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def value(self):
        return self.value

    def next(self):
        return self.next


class SingleList():
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def find(self, value):
        current = self.head

        while current:
            if current.value == value:
                return current
            current = current.next

        return None

    def delete(self, node):
        previous = None
        current = self.head
        found = False

        while current is not None and not found:
            if current == node:
                found = True
            else:
                previous, current = current, current.next

        if found and previous is None: # Head is the node
            self.head = current.next
        else:
            previous.next = current.next

    def values(self):
        '''
        Returns a list contains all elements.
        '''
        result = []
        current = self.head
        while current:
            result.insert(0, current.value)
            current = current.next
        return result

