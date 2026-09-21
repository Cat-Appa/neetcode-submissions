class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(nums) - 1

        # enumerate() go over every index and pair it as (index, value).
        # Then it requires to be housed as list.
        result = list(enumerate(nums))

        # lambda is a custom function. Since pairs are (index, value),
        # sorting by using key as x[1] makes this list sorted based on value.
        result.sort(key = lambda x:x[1])

        #array = []
        # two pointer usually goes like this to prevent overlap.
        while p1 < p2:
            # if values adding together are equal to target
            if result[p1][1] + result[p2][1] == target:
                #array.append(result[p1][0])
                #array.append(result[p2][0])
                return sorted([result[p1][0], result[p2][0]])
            elif result[p1][1] + result[p2][1] > target:
                p2 -= 1
            else:
                p1 += 1
        