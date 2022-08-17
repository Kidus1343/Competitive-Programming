class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        N = len(nums)
        pre = nums[0]
        ans = 0
        
        for i in range(1, N):
            cur = nums[i]
            if cur <= pre:
                ans += pre - cur + 1
                cur = pre + 1
            pre = cur
            
        return ans
