# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
#   ```
#   Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#   Output: 7 -> 0 -> 8
#   Explanation: 342 + 465 = 807.
#   ```


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy, p, q = ListNode(0), l1, l2

        cur = dummy
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            s = x + y + carry
            carry = 0 if s < 10 else 1
            cur.next = ListNode(s % 10)
            p = p.next if p else p
            q = q.next if q else q
            cur = cur.next

        if carry > 0:
            cur.next = ListNode(carry)

        return dummy.next


def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l3 = Solution().addTwoNumbers(l1, l2)
    assert l3.val == 7
    assert l3.next.val == 0
    assert l3.next.next.val == 8
    print(l3)


if __name__ == "__main__":
    main()
