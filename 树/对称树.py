# 给定一个二叉树，检查它是否是镜像对称的。

# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

#     1
#    / \
#   2   2
#    \   \
#    3    3

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/symmetric-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处
#递归求解
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        对称树的特点在于镜像对称，递归的主要点是找到终止条件和递归原则
        该题，对应的点是否一致(终止条件)，对应的条件是，左子树的左右与右子树的右左一致（递归原则）
        """
        def isEqure(left,right):
        	# 终止条件
            if not (left or right):#两个都为空
                print('q')
                #not (left and right)
                return True
            if not (left and right):##有一个为空
                print('1')
            # not (left or right)
                return False
            if left.val!=right.val:#值不等
                print('2')
                return False
            print(left.val,right.val)
            return isEqure(left.left,right.right) and isEqure(left.right,right.left)
        if not root:
            return True
        return isEqure(root,root)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        在使用迭代的方法时，相当于用某一个容器来模拟递归的规则，在这个例子中，我选择了列表来完成，其他容器也可选择e
        队列，栈，双向队列。但是编辑器似乎不允许使用，我在import时没有成功
        """
        if not root:
            return True
        #from queue import Queue,LifoQueue,PriorityQueue
        que=[]
        que.append(root.left)
        que.append(root.right)
        while que:
            

            left= que.pop()
            right= que.pop()#默认--1
            
            if  (left is None) and (right is None):
                continue
            if  (left is None) or (right is None):
                print('a')
                return False
            if left.val!=right.val:
                print('b')
                return False
            #print(left.val,right.val)
    
            que.append(left.right)

            que.append(right.left)

            que.append(left.left)

            que.append(right.right)
        return True