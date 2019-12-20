# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：

# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。

# 示例 2：

# 输入: "cbbd"
# 输出: "bb"

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s=len(s)
        Ilist=[0]*len_s
        olist=[0]*len_s
        log=''
        len_i=0
        len_l=0
        for i in range(0,len_s):
            for j in range(0,i+1):
                if i-j<=1:#如果是它本身或者隔壁
                    if s[i]==s[j]:
                        Ilist[j]=1
                        len_i=i-j+1
                        if len_l<len_i:
                            log=s[j:i+1]
                            len_l=len_i
                else:
                    if s[i]==s[j] and olist[j+1]:
                        len_i=i-j+1 
                        Ilist[j]=1
                        if len_l<=len_i:
                            log=s[j:i+1]
                            len_l=len_i
            olist=Ilist
            Ilist=[0]*len_s
        return log