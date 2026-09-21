class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        # initialize pointers
        p1 = 0
        p2 = len(nums) - 1

        # there are multiple cases 
        while p2 >= p1:
            if nums[p1] == val:
                if nums[p2] != val:
                    nums[p1] = nums[p2]
                    p1 += 1
                    p2 -= 1
                    k += 1
                    
                elif nums[p2] == val:
                    p2 -= 1
            elif nums[p1] != val:
                p1 += 1
                k += 1
        return k