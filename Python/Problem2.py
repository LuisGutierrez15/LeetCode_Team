from typing import List


class Problem2:

    def minPatches(self, nums: List[int], n: int) -> int:
        initial_length: int = len(nums)
        missing: int = 1
        i: int = 0

        while missing <= n:
            try:
                if nums[i] <= missing:
                    missing += nums[i]
                else:
                    nums.append(missing)
                    nums.sort()
                    missing += missing
                    print("When added ", nums)

                i += 1
            except:
                nums.append(n)

        print("Final ", nums)

        return len(nums) - initial_length


dummy: List[int] = [1, 2, 5, 20]
n_dummy: int = 46


s: Problem2 = Problem2()

result = s.minPatches(dummy, n_dummy)

print(result)
