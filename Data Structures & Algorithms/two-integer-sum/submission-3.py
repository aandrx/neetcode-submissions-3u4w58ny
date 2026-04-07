class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # insert everything into a set, then check for sums
        # sort the items, then check?
        # if target - num[1] = (exists in list)

        # sorting sol
        # make copy and sort ascending 
        # use pointer at front and back 
        # iterate both pointers, if sum of nums is equal to target, ret
        # if less than target, inc left pointer, if greater, inc right pointer
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        
        A.sort()
        i, j = 0, len(nums) - 1 
        while i < j:
            cur = A[i][0] + A [j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []

        # for hashmap solution: 
        # make map to store values and indices of each element
        # iterate through array and compute complement of current element 
        # check if complement exists in map -> return indices of current element and complement
        # else return empty arr
        indices = {} # val -> index
        for i, n in enumerate(nums):
            indices[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []

        # hash map one pass -> check if complement of current element exists in map
        # create empty map -> for holding val, index
        # iterate through array 
        prevMap = {} # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i