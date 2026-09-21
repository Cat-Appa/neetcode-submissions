class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # use for loop to go over the array and if value = val, set it as -1
        for value in range(len(nums)):
            if nums[value] == val:
                nums[value] = -1

        # reverse sort and return k
        nums.sort(reverse=True)

        k = 0

        for value in range(len(nums)):
            if nums[value] != -1:
                k += 1
        return k