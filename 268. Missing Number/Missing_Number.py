class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = int(sum(nums))
        sum2 = int(len(nums))
        sum3 = int(sum2*(sum2 + 1) / 2)
        return sum3 - sum1
