class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                left_val = self.isSameTree(p.left, q.left)
                right_val = self.isSameTree(p.right, q.right)
                # print("left {0}, right {1}".format(left_val, right_val))
                return left_val and right_val


if __name__ == '__main__':
    p_left = TreeNode(2)
    p_right = TreeNode(5)
    p = TreeNode(1, p_left, p_right)
    q_left = TreeNode(2)
    q_right = TreeNode(3)
    q = TreeNode(1, q_left, q_right)
    TreeNode().isSameTree(p, q)
    print(TreeNode().isSameTree(p, q))
