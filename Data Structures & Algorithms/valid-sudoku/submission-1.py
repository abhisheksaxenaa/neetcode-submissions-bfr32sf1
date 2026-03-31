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
                val = board[i][j]
                boxindex = (3 * (i // 3)) + (j // 3)
                if val == '.':
                    continue
                # check if in row, col or box
                if val in row[i] or val in col[j] or val in box[boxindex]:
                    # print(val)
                    return False
                row[i].add(val)
                col[j].add(val)
                box[boxindex].add(val)
        return True

