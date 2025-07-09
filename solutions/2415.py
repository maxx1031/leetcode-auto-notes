class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        flag = False
        while q:
            vals = []
            nodes = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:# perfect binary tree
                    q.append(node.left)
                    q.append(node.right)
                if flag:
                    vals.append(node.val)
                    nodes.append(node) # condidate level to reverse
            if flag:
                for val, node in zip(vals[::-1], nodes):
                    node.val = val
            flag = not flag
        return root

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q, level = [root], 0
        while q[0].left:
            q = list(chain.from_iterable((node.left, node.right) for node in q))
            
            if level == 0:
                for i in range(len(q) // 2):
                    x, y = q[i], q[-1-i]
                    x.val, y.val = y.val, x.val
            level ^= 1
        return root