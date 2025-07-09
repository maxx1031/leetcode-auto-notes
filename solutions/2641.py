from collections import deque, defaultdict

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.val = 0
        q = deque([root])
    
        while q:
            tmp = q
            next_level_sum = 0
            q = []
            # save next level nodes
            for node in tmp:
                if node.left:
                    q.append(node.left)
                    next_level_sum += node.left.val
                if node.right:
                    q.append(node.right)
                    next_level_sum += node.right.val
            # update node.left.val and right val
            for node in tmp:
                children_sum = (node.left.val if node.left else 0) + \
                               (node.right.val if node.right else 0)
                if node.left:
                    node.left.val = next_level_sum - children_sum
                if node.right:
                    node.right.val = next_level_sum - children_sum
      
        return root

