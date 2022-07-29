class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        operation = 0
        l, r = 0, len(nums) - 1
        for i in range(len(nums)):
            if nums[l] + nums[r] == k and r > l:
                l += 1
                r -= 1
                operation += 1
            elif nums[l] + nums[r] > k and r > l:
                r -= 1
            elif nums[l] + nums[r] < k and r > l:
                l += 1
        return operation
