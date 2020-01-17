# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
#   ```
#   Given nums = [2, 7, 11, 15], target = 9,
#
#   Because nums[0] + nums[1] = 2 + 7 = 9,
#   return [0, 1].
#   ```

from typing import List


class Solution1:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, n1 in enumerate(nums):
            for i2, n2 in enumerate(nums[i1+1:], start=i1+1):
                if n1 + n2 == target:
                    return [i1, i2]


class Solution2:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, n in enumerate(nums):
            hash_table[n] = i
        for k, i in hash_table.items():
            val = hash_table.get(target - k, '')
            if val != '' and i != val:
                return [i, val]


class Solution3:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, n in enumerate(nums):
            val = hash_table.get(target - n, '')
            if val != '' and i != val:
                return [val, i]
            else:
                hash_table[n] = i


def main():
    # nums = [2, 7, 11, 15], target = 9
    assert Solution1().twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert Solution2().twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert Solution3().twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]

    # nums = [3,2,4], target = 6
    assert Solution1().twoSum(nums=[3, 2, 4], target=6) == [1, 2]
    assert Solution2().twoSum(nums=[3, 2, 4], target=6) == [1, 2]
    assert Solution3().twoSum(nums=[3, 2, 4], target=6) == [1, 2]

    # NOTE: A hash table cannot have duplication keys. For this case, you
    # cannot use a simple key-value hash table.
    # nums = [3,3], target = 6
    # assert Solution1().twoSum(nums=[3, 3], target=6) == [0, 1]
    # assert Solution2().twoSum(nums=[3, 3], target=6) == [0, 1]
    # assert Solution3().twoSum(nums=[3, 3], target=6) == [0, 1]


if __name__ == "__main__":
    main()
