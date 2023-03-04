import functools
class Solution:
    def countDigitOne(self, num: int) -> int:
        val = str(num)
        n = len(val)
        
        @functools.lru_cache(None)
        def dp(i, count, tight):
            if i >= n:
                return count
            
            res = 0
            limit = int(val[i]) if tight else 9
                
            for d in range(limit + 1):
                res += dp(i + 1, count + (d == 1), tight & (d == limit))
            return res
        
        return dp(0,0,True)
    

