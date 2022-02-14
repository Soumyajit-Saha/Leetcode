class Solution:
    def canJump(self, nums: List[int]) -> bool:
#         if len(nums) == 1:
#             return True
#         dp = [False]*len(nums)
#         dp[-1] = True
#         for i in range(len(nums)-2, -1, -1):
#             for j in range(1, nums[i]+1):
#                 # print(dp[j])
#                 if(i+j <= len(nums) -1):
#                     dp[i] |= dp[i+j]
        
#         return dp[0]

        goal = len(nums)-1 # the last position

        for i in range(len(nums)-2, -1, -1): # move from 2nd last element to the 0th position element
            if i+nums[i] >= goal: #check if we can go to the goal position from this position
                goal = i # shift the goal towards left

        return True if goal==0 else False
