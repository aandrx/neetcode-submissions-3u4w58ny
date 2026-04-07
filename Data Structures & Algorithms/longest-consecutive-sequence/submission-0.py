class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # give list of ints, ret len of longest consecutive seq 
        
        # set? since uniques 
        # if set[num-1] exists, then it can continue -> finding the start of seq 
        # track longest so far 
        # checking num-1 -> NO PREDECESSOR, num is the START 
        # when tracking length, its ok to do num+length since its consevutive, length is only ++ 
        # while the next consecutive num in set, inc length, update longest 
        # ^while because it should continuously check until consecutive is NOT in set

        numSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(length, longest)
        return longest



