class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Moore's Voting algo
        c=0
        me=float('infinity')
        for i in nums:
            if me==float('infinity'):
                me=i
                c=1
            else:
                if i!=me:
                    c-=1
                else:
                    c+=1
                if c==0:
                    me=i
                    c=1
        return me
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # My code
        map_={}
        for i in nums:
            if i not in map_.keys():
                map_[i]=1
            else:
                map_[i]+=1
        
        for i in map_:
            if map_[i]>len(nums)//2:
                return i
