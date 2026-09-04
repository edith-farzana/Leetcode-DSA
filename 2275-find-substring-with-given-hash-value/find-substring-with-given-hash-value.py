class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        current_hash = 0
        pk_minus_1 = pow(power, k - 1, modulo)
        
        for i in range(n - k, n):
            val = ord(s[i]) - ord('a') + 1
            current_hash = (current_hash + val * pow(power, i - (n - k), modulo)) % modulo
            
        result_index = -1
        
        if current_hash == hashValue:
            result_index = n - k
            
        for i in range(n - k, 0, -1):
            val_out = ord(s[i + k - 1]) - ord('a') + 1
            val_in = ord(s[i - 1]) - ord('a') + 1
            
            current_hash = (current_hash - val_out * pk_minus_1) % modulo
            current_hash = (current_hash * power + val_in) % modulo
            current_hash = (current_hash + modulo) % modulo
            
            if current_hash == hashValue:
                result_index = i - 1
                
        return s[result_index : result_index + k]
