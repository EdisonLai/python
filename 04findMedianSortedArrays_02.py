
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list_len = len(nums1) + len(nums2)
        list = []
        m, n = 0, 0

        if not len(nums1):
            list += nums2[:len(nums2) // 2 + 1]
        elif not len(nums2):
            list += nums1[:len(nums1) // 2 + 1]
        else:
            for i in range(list_len // 2 + 1):
                if nums1[m] <= nums2[n]:
                    list.append(nums1[m])
                    m += 1
                    if m >= len(nums1):
                        list += nums2[n:n + list_len // 2 + 1 - len(list)]
                        break
                if nums2[n] <= nums1[m]:
                    list.append(nums2[n])
                    n += 1
                    if n >= len(nums2):
                        list += nums1[m:m + list_len // 2 + 1 - len(list)]
                        break

        if list_len % 2 == 0:
            return (list[list_len // 2 - 1] + list[list_len // 2])/2
        else:
            return list[list_len // 2]

list1 = [2]
list2 = [1, 3, 4]
solve = Solution()
result = solve.findMedianSortedArrays(list1, list2)
print(result)