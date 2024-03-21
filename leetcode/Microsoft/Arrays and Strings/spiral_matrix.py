from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        col = len(matrix[0])
        row = len(matrix)
        no_of_elements = col * row
        left = up = 0
        right = col - 1
        down = row - 1
        spiral_elements = []

        while len(spiral_elements) < no_of_elements:

            # traverse from left to right
            for c in range(left, right+1):
                spiral_elements.append(matrix[up][c])
            # traverse from up to down
            for r in range(up+1, down+1):
                spiral_elements.append(matrix[r][right])

            if up != down:
                # traverse from right to left
                for c in range(right-1, left-1, -1):
                    spiral_elements.append(matrix[down][c])
            if left != right:
                # traverse from down to up
                for r in range(down-1, up, -1):
                    spiral_elements.append(matrix[r][left])
            left += 1
            right -= 1
            up += 1
            down -= 1

        return spiral_elements


if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
