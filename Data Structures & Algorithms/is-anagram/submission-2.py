class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # checking string = string, orders can be different 
        # dont have to sort, create an array of the size, then count freq on each idex of the arr for letter 

        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
        