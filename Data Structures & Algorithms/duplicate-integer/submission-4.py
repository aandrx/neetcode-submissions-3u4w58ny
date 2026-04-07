class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # do double if, check if current looks like any other element
        for i in range(len(nums)) :
            for j in range(i + 1, len(nums)) :
                if nums[i] == nums[j]:
                    return True
        return False

        # sort first, then do this vs next
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

        # use hash set to keep track of seen and then cross check with seen
        seen = set()
        # for each item, add to set, if already in set == duplicate, then return 
        for num in nums:
            if num in seen:
                return True
            nums.add(num)
        return False

        # hash set length => since only uniques in hash sets, if the final set length < original list, then = dupes
        return len(set(nums)) < len(nums)