class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(nums) - 1
        result = list(enumerate(nums))

        result.sort(key = lambda x:x[1])

        array = []

        while p1 < p2:
            if result[p1][1] + result[p2][1] == target:
                array.append(result[p1][0])
                array.append(result[p2][0])
                return sorted([result[p1][0], result[p2][0]])
            elif result[p1][1] + result[p2][1] > target:
                p2 -= 1
            else:
                p1 += 1
        