class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # given ints nums, ret arr where output[i] is product of all elements except nums[i]
        # product guaranteed to fit 32 bits 
        # solve in O(n) without using division? 

        # COULD map it 
        # how to skip an index? 
        # while index != i

        # prefix and suffix -> do product of prefix, product of suffix 
        # pref -> for i from i to n
        # suff -> for n - 2, -1, -1 
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        # idea here is that no prefix if the number is 0
        # there is no suffix if the number is the "last" in the list 
        # prefix is still multiplied though, so set it to 0 (suffix too) 
        pref[0] = suff[n - 1] = 1 # nothing to left of pref[0], nothing to right of suff[n-1]

        for i in range(1, n): # goes from 1 to n - 1
            pref[i] = nums[i - 1] * pref[i - 1] # i - 1, since the range starts from 1
        for i in range(n - 2, -1, -1): # goes from n - 2 to 0 (0 - 1)
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n): # assemble this product for all terms in nums 
            res[i] = pref[i] * suff[i] 
        return res 

