class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # given arr of ints incrasing order 

        # 2 pointers -> tracking until you hit the sum 
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [1 + l, 1 + r]
        return []
