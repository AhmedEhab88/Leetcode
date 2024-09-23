# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if (p.val > root.val and q.val < root.val) or (
            p.val < root.val and q.val > root.val
        ):
            return root
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)


node1 = TreeNode(6)
node1.left = TreeNode(2)
node1.left.right = TreeNode(4)
node1.left.right.right = TreeNode(5)
node1.left.right.left = TreeNode(3)
node1.left.left = TreeNode(0)
node1.right = TreeNode(8)
node1.right.right = TreeNode(9)
node1.right.left = TreeNode(7)


obj = Solution()

print(obj.lowestCommonAncestor(node1, node1.left, node1.left.right).val)
