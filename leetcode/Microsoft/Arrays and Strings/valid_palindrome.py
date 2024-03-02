class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        # abccba
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
        return True


# ######## Partially Working ########
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         clean_str = ""
#         for l in s.lower():
#             if l.isalnum():
#                 l.join(clean_str)
#                 clean_str += l
#
#         str_len = len(clean_str)
#         # print(str_len)
#         first_half = clean_str[:int(str_len / 2)]
#         # print(first_half)
#         if str_len % 2 == 0:
#             # print("even")
#             for i in range(str_len-1, int(str_len/2)-1, -1):
#                 if clean_str[i] != clean_str[str_len-1-i]:
#                     return False
#         else:
#             # print("odd")
#             for i in range(str_len-1, int(str_len/2), -1):
#                 if clean_str[i] != clean_str[str_len-1-i]:
#                     return False
#
#         return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(s="A man, a plan, a canal: Panama"))  # A man, a plan, a canal: Panama
