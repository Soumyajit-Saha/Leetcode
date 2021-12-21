class Solution:
    def firstUniqChar(self, s: str) -> int:
        map_={}
        for i in range(len(s)):
            if s[i] not in map_.keys():
                map_[s[i]]=1
            else:
                map_[s[i]]+=1
        
        for i in map_.keys():
            if map_[i]==1:
                for j in range(len(s)):
                    if i==s[j]:
                        return j
        return -1
