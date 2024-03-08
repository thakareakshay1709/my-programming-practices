class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        str_len = len(s)
        result = 0
        print(f"initial string {s} with {str_len} chars")
        str_without_spaces = ""
        # leading whitespaces
        for i in range(0, str_len):
            if s[i] == ' ':
                continue
            str_without_spaces += s[i:]
            break

        if str_without_spaces == "":
            return 0
        print(f"{str_without_spaces} without spaces with {len(str_without_spaces)} chars")
        # leading characters
        if str_without_spaces[0].isalpha():
            return 0
        # check positive or negative
        pos_or_neg = 1
        if str_without_spaces[0] == "+":
            pos_or_neg = 1
            str_without_spaces = str_without_spaces[1:]
        elif str_without_spaces[0] == "-":
            pos_or_neg = -1
            str_without_spaces = str_without_spaces[1:]
        print(f"{str_without_spaces} without spaces with {len(str_without_spaces)} chars")

        # Step 3
        ch = 0
        while ch < len(str_without_spaces) and str_without_spaces[ch].isdigit():
            number = int(str_without_spaces[ch])

            # Check overflow and underflow conditions.
            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and number > INT_MAX % 10):
                # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.
                return INT_MAX if pos_or_neg == 1 else INT_MIN
            result = 10 * result + number
            ch += 1

        return result * pos_or_neg


if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi(" "))
