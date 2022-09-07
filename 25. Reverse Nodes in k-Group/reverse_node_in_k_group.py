class Solution:
    def reverseKGroup(self, head, k):
        anchor = jump = ListNode(0)
        anchor.next = left = right = head
        

        while True:
            next_len = 0

            while right and next_len < k:
                
                right = right.next
                next_len += 1
                
            if next_len == k:
               
                prev, cur = right, left
                for _ in range(k):
                    nxt = cur.next
                    cur.next = prev
                    cur, prev = nxt, cur

               

                jump.next = prev
                jump, left = left, right

            else:
                return anchor.next
