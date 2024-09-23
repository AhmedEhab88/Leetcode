# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return None
        res, queue, hashMap, curLevel = [], [], {}, 0
        queue.append(root)
        hashMap[root] = curLevel
        while len(queue) > 0:
            node = queue.pop(0)
            curLevel = hashMap[node]
            if len(res) < curLevel + 1:
                res.append([node.val])
            else:
                res[curLevel].append(node.val)
            if node.left:
                queue.append(node.left)
                hashMap[node.left] = curLevel + 1
            if node.right:
                queue.append(node.right)
                hashMap[node.right] = curLevel + 1
        return res


obj = Solution()

# node1 = TreeNode(6)
# node1.left = TreeNode(2)
# node1.left.right = TreeNode(4)
# node1.left.right.right = TreeNode(5)
# node1.left.right.left = TreeNode(3)
# node1.left.left = TreeNode(0)
# node1.right = TreeNode(8)
# node1.right.right = TreeNode(9)
# node1.right.left = TreeNode(7)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)


print(obj.levelOrder(root))
