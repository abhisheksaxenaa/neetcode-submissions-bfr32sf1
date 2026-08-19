class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        if R == 0:
            return False
        C = len(matrix[0])
        l = 0
        h = (R - 1) * C + (C - 1) # 11

        while (l <= h):
            mid = l + ((h - l) // 2) # 5
            i = mid // C
            j = mid % C
            # print(l, h, i, j, mid)
            # print("->",matrix[i][j])
            if matrix[i][j] < target:
                l = mid + 1
            elif matrix[i][j] > target:
                h = mid - 1
            else:
                return True
        return False