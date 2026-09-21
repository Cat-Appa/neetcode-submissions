class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = 1

        array = []
        for p1 in range(len(nums)):
            p2 = p1 + 1
            for p2 in range(p1 + 1, len(nums)):
                if nums[p1] + nums[p2] == target:
                    array.append(p1)
                    array.append(p2)
                    return array
            if nums[p1] + nums[p2] == target:
                array.append(p1)
                array.append(p2)
                return array
            
