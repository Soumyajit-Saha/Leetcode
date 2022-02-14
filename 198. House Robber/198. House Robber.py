class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)<3:
            return max(nums)
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0],nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        print(dp)    
        return dp[len(nums)-1]
