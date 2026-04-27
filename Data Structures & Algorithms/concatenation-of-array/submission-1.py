class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for x in 2 * nums:
            ans.append(x)
        
        return ans