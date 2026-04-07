class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # track the complement 
        # since i need to track the whole array as i go, use map 
        map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map:
                return [map[complement], i]
            else:
                map[nums[i]] = i
        return []