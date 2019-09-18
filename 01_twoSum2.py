from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dirt = {}
        for i, value in enumerate(nums):
            dirt[value] = i
        for i, value in enumerate(nums):
            tmp_num2 = target - value
            index = dirt.get(tmp_num2)
            if (index != None and index != i):
                return [i, index]

tmp = [2,5,5,11]
result= []
solve = Solution()
result = solve.twoSum(tmp, 10)
for index in result:
    print(' ', index)

