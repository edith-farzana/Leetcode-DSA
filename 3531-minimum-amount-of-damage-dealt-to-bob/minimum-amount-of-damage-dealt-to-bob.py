import functools

class Solution:
    def minDamage(self, power: int, damage: list[int], health: list[int]) -> int:
        enemies = []
        for d, h in zip(damage, health):
            t = (h + power - 1) // power
            enemies.append((d, t))
            
        def compare(e1, e2):
            d1, t1 = e1
            d2, t2 = e2
            if d1 * t2 > d2 * t1:
                return -1
            elif d1 * t2 < d2 * t1:
                return 1
            return 0
            
        enemies.sort(key=functools.cmp_to_key(compare))
        
        total_damage = 0
        current_time = 0
        
        for d, t in enemies:
            current_time += t
            total_damage += d * current_time
            
        return total_damage
