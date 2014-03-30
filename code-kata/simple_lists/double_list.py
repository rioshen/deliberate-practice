#!/usr/bin/env python

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleList():
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head.prev = node
        self.head = node

    def find(self, value):
        '''
        Return the node if found, else return None
        '''
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next

        return None

    def delete(self, node):
        previous = None
        found = False
        current = self.head

        while current is not None and not found:
            if current == node:
                found = True
            else:
                previous, current = current, current.next

        if found and previous:
            self.head = current.next
            current.next.prev = self.head
        else:
            previous.next = current.next
            current.next.prev = previous.next

    def values(self):
        result = []
        current = self.head

        while current:
            result.insert(0, current.value)
            current = current.next

        return result
