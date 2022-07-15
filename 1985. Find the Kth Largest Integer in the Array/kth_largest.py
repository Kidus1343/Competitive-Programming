class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums=sorted([int(x) for x in nums])
        return str(nums[-k])
