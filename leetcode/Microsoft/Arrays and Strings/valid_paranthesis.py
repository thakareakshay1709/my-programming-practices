class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        h_map = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in h_map:
                print(f"char : {char}")
                top_element = stack.pop() if stack else '#'
                if h_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()[]{}"))
