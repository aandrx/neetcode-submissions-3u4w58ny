class Solution:
    def isPalindrome(self, s: str) -> bool:
        # go through each index: if its invalid, skip it (both sides) 
        # after checking validity, then check equality 
        # two pointer 

        l, r = 0, len(s) - 1
        s = s.lower()

        while l < r:
            # validity checking 
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1 

        return True
            # equality checking 
            # iterate 


    def alphaNum(self, c) -> bool:
        return (
            ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )
