class Solution:
    def sumOfSquare(self, n):
        s=0
        while n > 0:
            d = n % 10
            s += d**2
            n = n//10
        return s
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            n=self.sumOfSquare(n)
            if n==1:
                return True
            if n in s:
                return False
            s.add(n)
