class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sety = set(nums)

        if len(sety) < len(nums):
            return True
        else:
            return False