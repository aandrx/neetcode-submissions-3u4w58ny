class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if dupe, ret true
        # else, ret false 

        # sort first, then start from idx 1, if idx1 = idx i-1, then dupe 
        if len(nums) == 0:
            return False

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

        
    