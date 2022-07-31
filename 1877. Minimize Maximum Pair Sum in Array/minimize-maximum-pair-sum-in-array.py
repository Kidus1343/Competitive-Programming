class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        minPairList = []
        for i in range(len(nums) // 2):
            minPairList.append(nums[i] + nums[len(nums) - 1 - i])

        return max(minPairList)
        
