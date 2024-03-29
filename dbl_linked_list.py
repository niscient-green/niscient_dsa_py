class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            if index < self.length / 2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length - 1, index, -1):
                    temp = temp.prev
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        else:
            return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        else:
            if index == 0:
                return self.prepend(value)
            elif index == self.length:
                return self.append(value)
            else:
                new_node = Node(value=value)
                before = self.get(index - 1)
                after = before.next

                new_node.prev = before
                new_node.next = after
                before.next = new_node
                after.prev = new_node

                self.length += 1
                return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            if index == 0:
                return self.pop_first()
            elif index == self.length - 1:
                return self.pop()
            else:
                temp = self.get(index)
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.next = None
                temp.prev = None
                self.length -= 1
                return temp

    def swap_first_last(self):
        if self.length <= 1:
            return False
        else:
            self.head.value, self.tail.value = self.tail.value, self.head.value
            return True

    def reverse(self):
        if self.length <= 1:
            # Error can't reverse a list of 0 or 1 nodes
            return False
        else:
            temp = self.head
            while temp is not None:
                # Swap the prev and next pointers of node points to
                temp.prev, temp.next = temp.next, temp.prev
                # Move to the next node
                temp = temp.prev
            # Swap the head and tail pointers
            self.head, self.tail = self.tail, self.head
            return True

    def is_palindrome(self):
        left = self.head
        right = self.tail

        while left != right:
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev

        return True

    def swap_pairs(self):
        if self.length <= 1:
            # Error: list is too short to swap
            return False
        else:
            left = self.head
            right = self.head.next
            while right is not None:
                left.value, right.value = right.value, left.value
                left = left.next.next
                if right.next is None:
                    right = None
                else:
                    right = right.next.next
            return True

