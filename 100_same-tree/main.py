from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p or not q:
            if not p and not q:
                return True
            return False
        return p.val == q.val and \
                   self.isSameTree(p.left, q.left) and \
                   self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    assert Solution().isSameTree(None, None)
    assert not Solution().isSameTree(None, TreeNode(10))
    assert not Solution().isSameTree(TreeNode(10), None)
    assert Solution().isSameTree(TreeNode(1), TreeNode(1))
    assert not Solution().isSameTree(TreeNode(1), TreeNode(2))
    assert Solution().isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)))
    assert not Solution().isSameTree(
        TreeNode(1, TreeNode(2)), TreeNode(1, right=TreeNode(2))
    )
