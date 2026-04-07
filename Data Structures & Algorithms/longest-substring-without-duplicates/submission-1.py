class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find len of longest substring with NO dupes 
        # no dupes -> sets ? 

        # map all chars to a set first 
        # two pointers -> compare, check if set, then continue 


        # whole idea: keep a set of the unique characters, in charSet 
        # calculation of length done with r - l for all cases 
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # if the character is in existing chars
            while s[r] in charSet:
                charSet.remove(s[l]) # remove the character 
                l += 1

            # if s[r] is unique (not in set yet)
            charSet.add(s[r])
            # calculate max 
            res = max(res, r - l + 1)
        return res