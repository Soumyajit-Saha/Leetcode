class Solution:
    l=[]
    def letterCombinations(self, digits: str) -> List[str]:
        map_={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.l=[]
        if digits=='':
            return self.l
        
        self.bk(digits,0,map_,'')
        
        return self.l
    
    def bk(self,digits,ind,map_,s):
        if ind>len(digits)-1:
            self.l.append(s)
        else:
            for i in map_[digits[ind]]:
                s=s+i
                self.bk(digits,ind+1,map_,s)
                s=s[:-1]
