from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # print(m, n)
        row, col = set(), set()

        for r in range(m):
            # print("r=", r)
            for c in range(n):
                # print("c=", c)
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)
                    print(f"found 0 at : {r}{c}")

        for r in range(m):
            for c in range(n):
                if r in row or c in col:
                    matrix[r][c] = 0
        return matrix


if __name__ == "__main__":
    sol = Solution()
    print(sol.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
