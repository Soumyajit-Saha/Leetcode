class Solution:
    ans=[]
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans=[]
        self.bk(n,'',0,0)
        return self.ans
    
    def bk(self,n,s,op,cl):
        if cl==n:
            self.ans.append(s)
        else:
            if op==cl:
                self.bk(n,s+'(',op+1,cl)
            elif op>cl:
                if op<n:
                    self.bk(n,s+'(',op+1,cl)
                self.bk(n,s+')',op,cl+1)
                
