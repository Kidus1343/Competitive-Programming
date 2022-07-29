class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        boolValues = []
        for i in range(len(l)):
            new = sorted(nums[l[i]: r[i] + 1])
            boolValues.append(self.isArithmetic(new))
        return boolValues
    
    def isArithmetic(self, newArray):
        for i in range(len(newArray) - 1):
            if newArray[i + 1] - newArray[i] != newArray[1] - newArray[0]:
                return False
        return True
