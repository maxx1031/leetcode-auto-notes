# 236. Lowest Common Ancestor of a Binary Tree

## 1. Clarifying Questions

What boundary conditions or constraints should I confirm with an interviewer before coding? (Provide at least 3 valuable questions with typical answers).

Q: **What should be returned if one or both of the nodes `p` and `q` are not present in the tree?**  
→ Typically, the function should return `None` if either node is not present in the tree.

Q: **Can the input tree be empty, and if so, what should be the output?**  
→ If the tree is empty, the output should be `None`.

Q: **Are the values of the nodes unique?**  
→ Yes, the values of the nodes are unique, which simplifies identification.

## 2. Algorithm & Data Structure

Briefly list the multiple core algorithmic approaches and required data structures to solve this problem.

- **Main Algorithm Category:** Tree Traversal
  - **Approach 1 Name:** Recursive Post-order Traversal
  - **Approach 2 Name:** Iterative using Parent Pointers
- **Data Structure:** Binary Tree

## 3. High-Level Description

Briefly describe the execution flow for each major approach.

### Approach 1: Recursive Post-order Traversal

- Traverse the tree starting from the root.
- Check if the current node is either `p` or `q`.
- Recursively search in the left and right subtrees.
- If both left and right subtrees return non-null, the current node is the LCA.
- If only one side returns non-null, return that side.

### Approach 2: Iterative using Parent Pointers

- Use a dictionary to map each node to its parent.
- Traverse the tree iteratively to fill this dictionary.
- Use the parent pointers to find the path from each node (`p` and `q`) to the root.
- Compare paths to find the deepest common node, which is the LCA.

## 4. Code (with Key Explanations)

Feature [My Code] as one of the solutions, adding concise, insightful comments. Additionally, provide clean, runnable Python code for the other major approaches described in Section 3.

```python
"""
Approach 1: Recursive Post-order Traversal
- Traverse the tree recursively.
- Base cases: if root is None or root matches p or q, return root.
- Recursively find LCA in left and right subtrees.
- If both sides return non-null, current node is LCA.
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
```

```python
"""
Approach 2: Iterative using Parent Pointers
- Use a dictionary to map each node to its parent while traversing the tree.
- Use sets to track the ancestors of p and q.
- The first common ancestor in the paths is the LCA.
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        stack = [root]
        
        # Populate parent dictionary
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        # Find ancestors of p
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        
        # Find the lowest common ancestor of q
        while q not in ancestors:
            q = parent[q]
        
        return q
```

## 5. Test Cases

Use a Markdown table to provide at least 5 representative test cases, covering normal, edge, and special scenarios.

| Case Description             | Input                          | Output | Explanation                                               |
|------------------------------|--------------------------------|--------|-----------------------------------------------------------|
| Both nodes are direct children | `root = [3,5,1], p = 5, q = 1` | `3`    | Both nodes are direct children of root.                   |
| One node is ancestor of the other | `root = [3,5,1], p = 5, q = 4` | `5`    | Node `5` is the ancestor of node `4`.                     |
| Nodes on different subtrees  | `root = [3,5,1,6,2], p = 6, q = 2` | `5`    | Nodes `6` and `2` are on different subtrees of node `5`.  |
| Tree with single node        | `root = [1], p = 1, q = 1`     | `1`    | Both nodes are the same and are the root.                 |
| Empty tree                   | `root = [], p = 1, q = 2`      | `None` | The tree is empty, so there is no LCA.                    |

## 6. Complexity

Use a Markdown table to analyze the time and space complexity for each major approach, including a brief justification.

| Approach                       | Time Complexity | Space Complexity                     |
|--------------------------------|-----------------|--------------------------------------|
| Recursive Post-order Traversal | O(N)            | O(H), for recursion stack            |
| Iterative using Parent Pointers| O(N)            | O(N), for storing parent pointers    |

## 7. Follow-Up & Optimizations

Propose 2-3 insightful follow-up questions or optimization directions.

- **How to handle streaming data?**  
  Consider using a data structure that supports dynamic updates, like a Union-Find with path compression.

- **How to validate more complex structures (e.g., AVL/Red-Black Trees)?**  
  Explore methods to efficiently find the LCA that also ensures tree balance properties are maintained.

- **What if you need to design a BST iterator?**  
  Implement an iterator using a stack to traverse the BST in-order, leveraging the properties of BSTs for efficient traversal.