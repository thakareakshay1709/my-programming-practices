from typing import List


class Solution:
    def reverseString(self, s: List[str]):
        """
        Do not return anything, modify s in-place instead.
        """

        # rev_input = []
        # for i in range(len(s)-1, -1, -1):
        #     rev_input.append(s[i])
        # return rev_input
        return s.reverse()


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseString(["h", "e", "l", "l", "o"]))
