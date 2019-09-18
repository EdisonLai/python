"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tmp_num = nums1 + nums2
        tmp_num.sort()
        if (len(tmp_num) % 2 == 0):
            result = (tmp_num[len(tmp_num) // 2 - 1] + tmp_num[len(tmp_num) // 2]) / 2
            return result
        else:
            result = (tmp_num[len(tmp_num) // 2])
            return result

list1 = [1, 2]
list2 = [3, 4]
solve = Solution()
result = solve.findMedianSortedArrays(list1, list2)
print(result)