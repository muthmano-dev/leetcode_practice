# Problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = 0
        if len(nums) != 0:
            num = 1 # We are tracking the change in the value
            for i in range(1, len(nums)):
                if nums[i] != nums[i-1]:
                    nums[num] = nums[i]
                    num += 1
                
        return num
