'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        if x:
            self.head = self
            self.tail = self
        else:
            self.head = None
            self.tail = None

    def append(self, x):
        if not self.head:
            self.val = x
            self.next = None
            self.head = self
            self.tail = self
        else:
            self.tail.next = ListNode(x)
            self.tail = self.tail.next

class Solution:
    def add_three_numbers(self, l1, l2, carry, result: ListNode):
        value = 0
        carry_tmp = 0
        if not (l1 or l2 or carry != 0) :
            return result

        if l1:
            value += l1.val
        if l2 :
            value += l2.val
        value += carry

        result_node = ListNode(value%10)
        if (result):
            result.next = result_node

        carry_tmp = value // 10

        self.add_three_numbers(l1.next if l1 else l1, l2.next if l2 else l2, carry_tmp, result_node)

        return result_node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.add_three_numbers(l1, l2, 0, None)


list1 = [2, 4, 3]
list2 = [5, 6, 4]

plist1 = ListNode(0)
plist2 = ListNode(0)

for value in list1:
    plist1.append(value)
for value in list2:
    plist2.append(value)
solve = Solution()
result = solve.addTwoNumbers(plist1, plist2)

