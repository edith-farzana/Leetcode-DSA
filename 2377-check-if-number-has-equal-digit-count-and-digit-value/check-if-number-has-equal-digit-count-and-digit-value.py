class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            expected_count = int(num[i])
            actual_count = num.count(str(i))
            if expected_count != actual_count:
                return False
        return True
