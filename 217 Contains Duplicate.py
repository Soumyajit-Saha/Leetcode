class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map_={}
        for i in nums:
            if i not in map_.keys():
                map_[i]=1
            else:
                return True
        return False
