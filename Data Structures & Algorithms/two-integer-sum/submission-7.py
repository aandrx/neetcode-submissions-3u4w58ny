class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # track a map that holds my resulting indices 
        # track the complement, since im given the target 
        map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map:
                return [map[complement], i]
            else:
                map[nums[i]] = i
        return []

        