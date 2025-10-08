class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Come back here when you are done with LINKED LISTS
        """
        linked_list = LinkedList(nums[0])
        for i, num in enumerate(nums):
            if i > 0:
                linked_list.append(num)
        linked_list.move_head_back(k)
        nums[:] = linked_list.to_array()


class LinkedList:
    def __init__(self, value):
        node = Node(value, None, None)
        node.next = node
        node.prev = node
        self.head = node
        self.tail = node
        self.len = 1

    def append(self, value):
        node = Node(value, self.head, self.tail)
        self.tail.next = node
        self.tail = node
        self.head.prev = node
        self.len += 1

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def move_head_back(self, k):
        k = k % self.len
        if k == 0:
            return
        self.head = self.tail
        for i in range(k - 1):
            self.head = self.head.prev

    def to_array(self):
        nums = []
        head = self.head
        current_node = self.head
        next_node = current_node.next
        while next_node != head:
            nums.append(current_node.value)
            current_node = next_node
            next_node = next_node.next
        nums.append(current_node.value)
        return nums


class Node:
    def __init__(self, value, next, prev):
        self._value = value
        self._next = next
        self._prev = prev

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        self._prev = prev

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
