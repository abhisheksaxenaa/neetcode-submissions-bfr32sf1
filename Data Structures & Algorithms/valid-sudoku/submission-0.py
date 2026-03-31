class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = []
        col = []
        box = []
        for _ in range(9):
            row.append(set())
            col.append(set())
            box.append(set())
        # formula for each cell number
        # R * i + c
        # i = 0,1,2 j = 0,1,2
        R = 9
        C = 9
        for i in range(R):
            for j in range(C):
                boxindex = (3 * (i // 3)) + (j // 3)
                if board[i][j] == '.':
                    continue
                # check if in row, col or box
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[boxindex]:
                    # print(board[i][j])
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[boxindex].add(board[i][j])
        return True

