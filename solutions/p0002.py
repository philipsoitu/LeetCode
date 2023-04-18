# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)

    def printlist(self):
        ans = ""
        currNode = self
        while currNode != None:
            ans += str(currNode.val)+" -> "
            currNode = currNode.next
        return ans


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        ans = ListNode()
        curr = ans
        prev = None
        while l1 != None or l2 != None or carry != 0:
            if l1 != None:
                val1 = l1.val
            else:
                val1 = 0
            if l2 != None:
                val2 = l2.val
            else:
                val2 = 0

            total_sum = val1 + val2 + carry
            curr.val = total_sum % 10
            carry = total_sum//10
            if prev != None:
                prev.next = curr
            prev = curr
            curr = ListNode()
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        return ans


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(7)))

print(Solution.addTwoNumbers(Solution, l1, l2).printlist())
