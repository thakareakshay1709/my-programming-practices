class Solution:
    def reverseWords(self, s: str) -> str:
        input_str = s.strip()
        if input_str == "":
            return ""
        split_str = input_str.split(" ")
        reverse_str = ""
        for i in range(len(split_str) - 1, -1, -1):
            if split_str[i] == "":
                continue
            reverse_str = reverse_str + split_str[i].strip() + " "
        return reverse_str.strip()


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords("a good   example"))
