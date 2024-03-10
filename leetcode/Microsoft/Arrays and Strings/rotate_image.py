from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, mat):
        m = len(mat)
        print(f"{m} cols matrix")
        for i in range(m):
            print(f"i={i}")
            for j in range(i + 1, m):
                print(f"j={j}, prev {mat[i][j]}{mat[i][j]}")
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
                print(f"j={j}, after {mat[i][j]}{mat[i][j]}")

    def reflect(self, mat):
        m = len(mat)
        for i in range(m):
            print(f"i={i}, m//2={m // 2}")
            for j in range(m // 2):
                print(f"prev={mat[i][j]}, {mat[i][-j - 1]}, {-j - 1}")
                mat[i][j], mat[i][-j - 1] = mat[i][-j - 1], mat[i][j]
                print(f"after={mat[i][-j - 1]}, {mat[i][j]}")


if __name__ == "__main__":
    sol = Solution()
    print(sol.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
