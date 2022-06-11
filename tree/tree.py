# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root, res):
        if not root:
            return None
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)


if __name__ == '__main__':
    three = TreeNode(3)
    two = TreeNode(2,three)
    one = TreeNode(1,None,two)
    s = Solution()
    print(s.inorderTraversal(one))
