class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_valid_palindrome(i, j):
            start = i
            end = j-1
            # i, j = 0, len(s) - 1
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        for l in range(len(s), 0, -1):
            for st in range(len(s) - l + 1):

                if is_valid_palindrome(st, st + l):
                    return s[st: st + l]
        return ""


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("bcabad"))
