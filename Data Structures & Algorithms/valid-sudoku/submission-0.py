class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for each row:
        # add seen values WITHIN that row into a set
        # "." is empty: continue 
        # if there is another occurence of a number, ret false
        # otherwise just add the value to the set at [row][i] 

        # check the same thing for columns -> swap the params, since its row, col 

        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True
