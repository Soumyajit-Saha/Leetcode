class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            sample_bit = n >> i
            sample_bit = sample_bit & 1
            res = res << 1
            res = res | sample_bit 
        return res
            
