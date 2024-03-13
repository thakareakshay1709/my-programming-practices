from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        size = len(height)
        for i in range(1, size - 1):
            print(i)
            left_max, right_max = 0, 0
            for j in range(i, 0, -1):
                print(f"value of left j={j}")
                left_max = max(left_max, height[j])
                print(f"left max = {left_max}")
            for j in range(i, size):
                print(f"value of right j={j}")
                right_max = max(right_max, height[j])
                print(f"right max = {right_max}")

            water += min(left_max, right_max) - height[i]
        return water


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
