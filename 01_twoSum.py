from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        index = 0
        for i in range(len(nums)):
            tmp_num2 = target - nums[i]
            try:
                index = nums.index(tmp_num2, i+1, len(nums))
            except ValueError:
                i += 1
            else:
                return [i, index]




tmp = [3,2,4]
result= []
solve = Solution()
result = solve.twoSum(tmp, 6)
for index in result:
    print(' ', index)

