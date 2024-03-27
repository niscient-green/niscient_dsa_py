# Node that holds a value and a pointer
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Queue that holds values, FIFO
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            # Add to the last end
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        else:
            temp = self.first
            if self.length == 1:
                self.first = None
                self.last = None
            else:
                self.first = self.first.next
            temp.next = None
            self.length -= 1
            return temp
