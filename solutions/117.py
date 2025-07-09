from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node': # type: ignore
        if not root:
            return None
        q = deque([root])
        while q:
            size = len(q)
            prev = None
            for _ in range(size):
                node = q.popleft()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)