from typing import List


class Problem2:

    def minPatches(self, nums: List[int], n: int) -> int:
        length: int = len(nums)
        missing: int = 1
        i: int = 0
        count: int = 0
        while missing <= n:
            if i < length and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                missing += missing
                count += 1

        return count


dummy: List[int] = [1, 2, 5, 20]
n_dummy: int = 46


s: Problem2 = Problem2()

result = s.minPatches(dummy, n_dummy)

print(result)
