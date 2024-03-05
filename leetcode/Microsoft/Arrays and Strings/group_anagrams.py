import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for chars in strs:
            anagrams[tuple(sorted(chars))].append(chars)
        print(anagrams)
        return anagrams.values()


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
