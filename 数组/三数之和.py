# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        nums=sorted(nums)
        record=[]
        if nums[0]>0:
            return record
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        print(hashmap)
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]==nums[l+1]:
                l +=1
            if nums[r]==nums[r-1]:
                r -=1
            if nums[l]+nums[r] in hashmap:
                record.append([nums[l],nums[r],hashmap[nums[l]+nums[r]]])
            l +=1
            r -=1
        return record