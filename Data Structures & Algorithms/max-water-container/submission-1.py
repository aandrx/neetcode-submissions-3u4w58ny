class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # find tallest bar 
        # store max as i go through 
        # two pointer -> calculate area after moving left/right, if greater than max, reassign 

        l, r = 0, len(heights) - 1
        max_value = 0

        while l < r:
            # calculate, then move left, calculate, then move right
            area = min(heights[l], heights[r]) * (r - l)
            max_value = max(max_value, area)
            # conditional: if heights of left <= heights of right, iterate left, otherwise iterate right 
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_value


