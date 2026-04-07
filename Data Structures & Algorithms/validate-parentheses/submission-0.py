class Solution:
    def isValid(self, s: str) -> bool:
        # every open bracket must be closed by same type of close bracket 
        # open brackets closed in correct order 
        # close has correct open 
        # ret true if s is valid, else false 

        # create a map first that maps the correct closing to correct opening 
        closing = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }
        stack = []

        for c in s:
            if c in closing:
                if stack and stack[-1] == closing[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        

        
