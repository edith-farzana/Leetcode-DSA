import math
from collections import Counter

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        half = (n + 1) // 2
        start = 10 ** (half - 1)
        end = 10 ** half
        
        valid_multisets = set()
        
        
        for i in range(start, end):
            s = str(i)
            if n % 2 == 0:
                p_str = s + s[::-1]
            else:
                p_str = s + s[:-1][::-1]
           
            if int(p_str) % k == 0:
                
                sorted_digits = "".join(sorted(p_str))
                valid_multisets.add(sorted_digits)
                
        total_good = 0
        fact = [math.factorial(x) for x in range(n + 1)]
        

        for digits in valid_multisets:
            counts = Counter(digits)
            
            denom = 1
            for c in counts.values():
                denom *= fact[c]
            total_p = fact[n] // denom
            
          
            if counts['0'] > 0:
                denom_zero = fact[counts['0'] - 1]
                for d, c in counts.items():
                    if d != '0':
                        denom_zero *= fact[c]
                zero_p = fact[n - 1] // denom_zero
            else:
                zero_p = 0
                
            total_good += (total_p - zero_p)
            
        return total_good
