class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort first each item in the list first, 
        # hash map with each key as the sorted version of a string, and val is list of strings belonging to that group
        # sort characters of string to form key
        # append origina string to list corresponding to the key 

        # start dict 
        # for every character in the word, check ord of character and then add to freq map if necessary 
        # map each letter to a count (in list)
        # for that word, append {count, word}
        # return list of res values 

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) # for this combo of frequencies, add the word 
        return list(res.values()) # for the resulting list, only return a list of the words