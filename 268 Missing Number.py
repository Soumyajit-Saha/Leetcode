class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        
        nums = set(nums)
        
        for i in range(1, l+1):
            if i not in nums:
                return i
        return 0
