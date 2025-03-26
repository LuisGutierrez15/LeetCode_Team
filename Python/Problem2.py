from typing import List
from itertools import combinations


class Problem2:
    # Useless because of itertools
    def factorial(self, n: int) -> int:
        if n < 0:
            raise ValueError("You cannot get the factorial of a negative number")

        return 1 if n == 0 else n if n == 1 else n * self.factorial(n - 1)

    # Useless because of itertools
    def possible_combinations(self, len_list: int) -> dict[int, int]:
        combinations: dict[int, int] = {}

        for r in range(1, len_list + 1):
            combinations[r] = self.factorial(len_list) // (
                self.factorial(r) * self.factorial(len_list - r)
            )

        return combinations

    # This whas a try of generating all combinations, useless because of itertools
    def all_combinations_WRONG(self, nums_list: List[int]) -> List[List[int]]:
        lista = []
        n_combinations = self.possible_combinations(len(nums_list))

        for key, value in n_combinations.items():
            for i in range(value):
                to_append: List = nums_list[i : i + key]
                if len(to_append) > 0 and to_append not in lista:
                    lista.append(to_append)

        return lista

    def all_combinations(self, nums_list: List[int]) -> List[List[int]]:
        combs = []
        for i in range(1, len(nums_list) + 1):
            combs.append(list(combinations(nums_list, i)))

        return combs

    def count(self, expected: List[int], nums: List[int]) -> int:
        count: int = 0
        real: List[int] = []
        possible_patches = self.possible_patches(nums, expected[-1])
        while True:
            combinations = self.all_combinations(nums)
            for comb in combinations:
                for c in comb:
                    new_number = sum(c)  # type: ignore
                    if new_number not in real and not new_number > expected[-1]:
                        real.append(new_number)

            real.sort()

            if expected == real:
                break

            try:
                nums.append(possible_patches[count])
                count += 1
            except:
                possible_patches = self.possible_patches(nums, expected[-1], True)
            finally:
                nums.sort()

        return count

    def possible_patches(self, nums: List[int], n: int, wide: bool = False):
        possible_patches: List[int] = (
            (
                [num for num in range(1, n)]
                if n % 2 == 0
                else [num for num in range(1, n)]
            )
            if wide
            else (
                [num for num in range(1, n) if n % num == 0 and num not in nums]
                if n % 2 == 0
                else [num for num in range(1, n) if n % num == 1 and num not in nums]
            )
        )
        print(possible_patches)
        return possible_patches

    def minPatches(self, nums: List[int], n: int) -> int:

        expected_list: List[int] = [x for x in range(1, n + 1)]

        return self.count(expected_list, nums)


dummy: List[int] = [1, 2, 5, 20]
n_dummy: int = 46


s: Problem2 = Problem2()

result = s.minPatches(dummy, n_dummy)

print(result)
