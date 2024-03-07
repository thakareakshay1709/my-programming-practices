from _ast import List


class Solution:
    def reverseWords(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        t = ''
        values = []
        for i in s:
            if i != ' ':
                t += i
            else:
                values.append(t)
                values.append(' ')
                t = ''

        values.append(t)

        flattened = [char for word in reversed(values) for char in word]
        s[:] = flattened
        return s


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords(["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]))
