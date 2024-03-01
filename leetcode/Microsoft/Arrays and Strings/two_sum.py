from typing import List


# Hashmap approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array_map = {}
        # saving indexes
        for i in range(len(nums)):
            array_map[nums[i]] = i

        for i in range(0, len(nums)):
            remaining = target - nums[i]
            if remaining in array_map and array_map[remaining] != i:
                return [i, array_map[remaining]]
        return []


# Brute force approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if (i != j) and (nums[j] + nums[i] == target):
                    return [i, j]
        return []


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum(nums=[2, 5, 5, 3], target=10))  # [1,2]
