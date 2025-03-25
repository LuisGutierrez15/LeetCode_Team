import itertools
from typing import List

def cleanPermutations(nums: List[int], num_list: int, req_nums: dict):
    permutations = []
    for i in range(len(nums)):
        permutations.extend(itertools.combinations(nums, i+1))

    permutations_sum = []
    for p in permutations:
        permutations_sum.append(sum(p))
                
    for p in permutations_sum:
        if(num_list.get(p) != None):
            num_list.pop(p)
    
    for i in num_list.keys():
        if(req_nums.get(i) == None):
            req_nums[i] = 1
        else:
            req_nums[i] += 1
        for j in permutations_sum:
            if(i - j > 0):
                if(req_nums.get(i - j) == None):
                    req_nums[i-j] = 1
                else:
                    req_nums[i-j] += 1

def minPatches(nums: List[int], n: int) -> int:
    num_list = {p+1: True for p in range(n)}
    req_nums = {}
    patches = 0

    cleanPermutations(nums, num_list, req_nums)
    
    while(num_list.keys()):
        req_nums = {k: v for k, v in sorted(req_nums.items(), key=lambda item: item[1]) if v > 1}
        print(req_nums)

        # max to min
        # max_key = max((k for k in req_nums if req_nums[k] == max(req_nums.values())), default=None)
        # min to max
        max_key = max(req_nums, key=req_nums.get)

        nums.append(max_key)
        req_nums.pop(max_key)
        patches += 1
        print(max_key)
        cleanPermutations(nums, num_list, req_nums)
    
    return patches


print(minPatches([1,10], 10))

        