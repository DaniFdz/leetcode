from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not other:
            return False
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        q = deque([root])

        while q:
            el = q.popleft()

            el.left, el.right = el.right, el.left

            if el.left:
                q.append(el.left)
            if el.right:
                q.append(el.right)

        return root


if __name__ == "__main__":
    s = Solution()
    assert s.invertTree(
        TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        )
    ) == TreeNode(
        4,
        TreeNode(7, TreeNode(9), TreeNode(6)),
        TreeNode(2, TreeNode(3), TreeNode(1))
    )
    assert s.invertTree(None) == None
