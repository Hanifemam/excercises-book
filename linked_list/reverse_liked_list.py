from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next=None, pre=None):
        self.val = val
        self._next = next
        self._pre = pre

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node) -> None:
        self._next = node

    @property
    def pre(self):
        return self._pre

    @pre.setter
    def pre(self, node) -> None:
        self._pre = node

    def __repr__(self) -> str:
        return f"ListNode{{val: {self.val}, next: {repr(self.next)}}}"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            curr.pre = nxt

            prev = curr
            curr = nxt
        return prev
