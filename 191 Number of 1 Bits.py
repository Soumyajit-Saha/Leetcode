class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        for i in range(32):
            sample_bit = (n >> i) & 1
            if sample_bit & 1 == 1:
                res+=1
        return res
