# 1291. 顺次数
# 显示英文描述

#     用户通过次数 804
#     用户尝试次数 913
#     通过次数 813
#     提交次数 2010
#     题目难度 Medium

# 我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。

# 请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）。

 

# 示例 1：

# 输出：low = 100, high = 300
# 输出：[123,234]

# 示例 2：

# 输出：low = 1000, high = 13000
# 输出：[1234,2345,3456,4567,5678,6789,12345]
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        l =len([int(char) for char in str(low)])
        h=len( [int(char) for char in str(high)])
        # print(high)
        pre=[]
        for i in range(l-1,h):
            # print(i)
            for x in range(1,10-i):
                sun=0
                s=x
                for j in range(i,-1,-1):
                    # print(j)
                    tep=10**j
                    # print(tep)
                    sun +=s*tep
                    # print(sun)
                    s+=1
                    # print(s)
                    # print(x)
                #print(sun)

                if sun<=high and sun>=low:
                    
                    pre.append(sun)
        return pre
#