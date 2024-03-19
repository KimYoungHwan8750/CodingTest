class Solution:
    def detectLoop(self, head):
        if not head or not head.next: return False
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False