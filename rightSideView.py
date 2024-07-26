# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If the tree is empty, return an empty list.
        if root is None:
            return []
        
        # List to store the right side view result.
        result = []
        
        # Initialize a queue to keep track of nodes at each level.
        q = Queue()
        
        # Start with the root node.
        q.put(root)
        
        # Continue the loop until the queue is empty.
        while not q.empty():
            # Get the number of nodes at the current level.
            size = q.qsize()
            
            # Iterate over all nodes at the current level.
            for i in range(size):
                # Get the front node from the queue.
                curr = q.get()
                
                # If it's the last node in the current level, add its value to the result list.
                if i == size - 1:
                    result.append(curr.val)
                
                # If the current node has a left child, add it to the queue.
                if curr.left is not None:
                    q.put(curr.left)
                
                # If the current node has a right child, add it to the queue.
                if curr.right is not None:
                    q.put(curr.right)
        
        # Return the right side view result.
        return result

        # The time complexity of this algorithm is O(n), 
        # where n is the number of nodes in the tree.
        # This is because each node is visited exactly once.
        
        # The space complexity is O(n) because, in the worst case,
        #  the queue can contain all the leaf nodes.
        # This happens when the tree is a complete binary tree, 
        # and there are n/2 leaf nodes in the last level.



######### Method 2 using DFS #######
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If the tree is empty, return an empty list.
        if root is None:
            return []
        
        # List to store the right side view result.
        self.result = []
        
        # Perform DFS starting from the root at level 0.
        self.dfs(root, 0)
        
        # Return the collected right side view nodes.
        return self.result
    
    def dfs(self, root: Optional[TreeNode], lvl: int) -> None:
        # Base case: if the node is None, return.
        if root is None:
            return
        
        # If the current level equals the size of the result list,
        # it means this is the first node we encounter at this level,
        # so we add it to the result.
        if lvl == len(self.result):
            self.result.append(root.val)
        
        # First, visit the right child (to ensure rightmost nodes are seen first),
        # then visit the left child.
        self.dfs(root.right, lvl + 1)
        self.dfs(root.left, lvl + 1)

        # The time complexity of this algorithm is O(n), where n is the number of nodes in the tree.
        # This is because each node is visited exactly once.
        
        # The space complexity is O(h), where h is the height of the tree.
        # This is because the recursion stack will have at most h function calls at a time.


        
        
