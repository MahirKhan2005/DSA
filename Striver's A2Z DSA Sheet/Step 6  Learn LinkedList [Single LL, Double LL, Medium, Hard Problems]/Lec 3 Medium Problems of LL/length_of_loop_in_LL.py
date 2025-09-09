class Solution:
    def findLengthOfLoop(self, head):
        fast = slow = head
        count = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                count=1
                slow=slow.next
                while fast!=slow:
                    count+=1
                    slow=slow.next
                return count
        return 0

