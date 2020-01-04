# 给定一个二叉树，找出其最大深度。

# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

# 说明: 叶子节点是指没有子节点的节点。

# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，

#     3
#    / \
#   9  20
#     /  \
#    15   7

# 返回它的最大深度 3 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        核心思想：记录每一次叶子节点所在的深度，使用max，求出最大深度。
        """
        stack=[]
        de=0
        if root is None:
            return 0
        stack.append((root,1))
        while stack!=[]:
           root,d= stack.pop()
           #de=max(d,de)
           #print(de)
           if root is not None:
               de=max(d,de)
               stack.append((root.left,d+1))
               stack.append((root.right,d+1))
           
        return de