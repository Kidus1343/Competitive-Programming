class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        prev="0"
        for i in range(n-1):
            prev=prev+"1"+self.invert(prev)
        return prev[k-1]

    def invert(self,s):
        ans=""
        for i in s[::-1]:
            if i=="0":
                ans+="1"
            else:
                ans+="0"
        return ans
