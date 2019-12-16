# 1290. 二进制链表转整数
# 显示英文描述

#     用户通过次数 1038
#     用户尝试次数 1057
#     通过次数 1051
#     提交次数 1261
#     题目难度 Easy

# 给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。

# 请你返回该链表所表示数字的 十进制值 。

 

# 示例 1：

# 输入：head = [1,0,1]
# 输出：5
# 解释：二进制数 (101) 转化为十进制数 (5)

# 示例 2：

# 输入：head = [0]
# 输出：0

# 示例 3：

# 输入：head = [1]
# 输出：1

# 示例 4：

# 输入：head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# 输出：18880

# 示例 5：

# 输入：head = [0,0]
# 输出：0

 

# 提示：

#     链表不为空。
#     链表的结点总数不超过 30。
#     每个结点的值不是 0 就
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        count=0
        sun=0
        p=head
        while 1:
            count+=1
            if p.next==None:
                break
            p=p.next
        #print(count)
        count -=1
        while 1:
            x=(2**count)*head.val
            sun +=x
            #print(sun)
            if head.next==None:
                break
            head=head.next
            count-=1
            
        return sun