from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    assert Solution().maxDepth(None) == 0

    assert (
        Solution().maxDepth(
            TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        )
        == 3
    )

    assert (Solution().maxDepth(TreeNode(1, None, TreeNode(2)))) == 2
