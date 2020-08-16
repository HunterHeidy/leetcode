# 5185. 存在连续三个奇数的数组
# 显示英文描述

#     通过的用户数 3543
#     尝试过的用户数 3562
#     用户总通过次数 3596
#     用户总提交次数 4789
#     题目难度 Easy

# 给你一个整数数组 arr，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回 true ；否则，返回 false 。

 

# 示例 1：

# 输入：arr = [2,6,4,1]
# 输出：false
# 解释：不存在连续三个元素都是奇数的情况。

# 示例 2：

# 输入：arr = [1,2,34,3,4,5,7,23,12]
# 输出：true
# 解释：存在连续三个元素都是奇数的情况，即 [5,7,23] 。

 

# 提示：

#     1 <= arr.length <= 1000
#     1 <= arr[i] <= 1000

#解法： 循环计算，遇到偶数重置
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<3:return False
        count=0
        for i in arr:
            if i%2==1:
                count+=1
                if count==3:return True
            else:count=0
        return False
