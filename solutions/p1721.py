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


class Solution(object):
    # convert to array
    def swapNodes(self, head, k):
        arr = []
        currNode = head
        while currNode != None:
            arr.append(currNode.val)
            currNode = currNode.next

        # swap
        temp = arr[k-1]
        arr[k-1] = arr[len(arr)+1-k]
        arr[len(arr)-(k-1)] = temp

        # convert to LL
        head = ListNode(arr[0])
        current = head

        for item in arr[1:]:
            new_node = ListNode(item)
            current.next = new_node
            current = new_node

        return head
