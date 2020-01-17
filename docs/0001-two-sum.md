# Two Sum

## Approach 1: Brute Force

The brute force approach is simple. Loop through each element `x` and find if there is another value that equals to `target - x`.

```python
class Solution1:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, n1 in enumerate(nums):
            for i2, n2 in enumerate(nums[i1+1:], start=i1+1):
                if n1 + n2 == target:
                    return [i1, i2]
```

### Complexity Analysis

Time complexity: `O(n^2)`

For each element, we try to find its complement by looping through the rest of array which takes `O(n)` time. Therefore, the time complexity is `O(n^2)`

Space complexity : `O(1)`

## Approach 2: Two-pass Hash Table

To improve our run time complexity, we need a more efficient way to check if the complement exists in the array. If the complement exists, we need to look up its index. What is the best way to maintain a mapping of each element in the array to its index? A [hash table](https://en.wikipedia.org/wiki/Hash_table).

We reduce the look up time from `O(n)` to `O(1)` by trading space for speed. A hash table is built exactly for this purpose, it supports fast look up in near constant time. I say "near" because if a collision occurred, a look up could degenerate to `O(n)` time. But look up in hash table should be amortized `O(1)` time as long as the hash function was chosen carefully.

A simple implementation uses two iterations. In the first iteration, we add each element's value and its index to the table. Then, in the second iteration we check if each element's complement (`target - nums[i]`) exists in the table. Beware that the complement must not be `nums[i]` itself!

```python
class Solution2:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, n in enumerate(nums):
            hash_table[n] = i
        for k, i in hash_table.items():
            val = hash_table.get(target - k, '')
            if val != '' and i != val:
                return [i, val]
```

### Complexity Analysis

Time complexity: `O(n)`

We traverse the list containing `n` elements exactly twice. Since the hash table reduces the look up time to `O(1)`, the time complexity is `O(n)`.

Space complexity : `O(n)`

The extra space required depends on the number of items stored in the hash table, which stores exactly `n` elements.

## Approach 3: One-pass Hash Table

It turns out we can do it in one-pass. While we iterate and inserting elements into the table, we also look back to check if current element's complement already exists in the table. If it exists, we have found a solution and return immediately.

```python
class Solution3:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, n in enumerate(nums):
            val = hash_table.get(target - n, '')
            if val != '' and i != val:
                return [val, i]
            else:
                hash_table[n] = i
```

### Complexity Analysis:

Time complexity : `O(n)`

We traverse the list containing `n` elements only once. Each look up in the table costs only `O(1)` time.

Space complexity : `O(n)`

The extra space required depends on the number of items stored in the hash table, which stores at most `n` elements.
