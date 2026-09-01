class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        max_count = 0

        for number in nums:
            if number == 1:
                current += 1
            else:
                if current > max_count:
                    max_count = current
                current = 0
        if current > max_count:
            return current
        else:
            return max_count