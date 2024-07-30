# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
################## Method 1 using DFS #############
class Solution:
  """
  Time Complexity: O(N), where N is the number of nodes in the tree.
  Space omplexity: O(h), where h is the height of the tree
  """
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # If the tree is empty, return False
        if root == None:
            return False
        
        # Initialize parent and level information for x and y
        self.x_parent = None
        self.x_lvl = -1
        self.y_parent = None
        self.y_lvl = -1
        
        # Perform DFS to find the parent and level of x and y
        self.dfs(root, 0, None, x, y)
        
        # x and y are cousins if they have different parents but the same level
        return self.x_parent != self.y_parent and self.x_lvl == self.y_lvl
    
    def dfs(self, root: Optional[TreeNode], lvl: int, parent: Optional[TreeNode], x: int, y: int):
        # Base case: if the current node is None, return
        if root == None:
            return
        
        # Check if the current node's value matches x or y and record the parent and level
        if root.val == x:
            self.x_parent = parent
            self.x_lvl = lvl
        if root.val == y:
            self.y_parent = parent
            self.y_lvl = lvl
        
        # Recur for left and right children, incrementing the level
        self.dfs(root.left, lvl + 1, root, x, y)
        self.dfs(root.right, lvl + 1, root, x, y)


############## Method 2: BFS ############
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
  """
  Time Complexity: O(N)
  Space Complexity: O(N), where N is the number of nodes in the tree.
  """
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # If the tree is empty, return False
        if root == None:
            return False
        
        x_found = False
        y_found = False
        
        # Initialize the queue for BFS
        q = Queue()
        q.put(root)
        
        while not q.empty():
            size = q.qsize()
            
            for i in range(size):
                curr = q.get()
                
                # Check if the current node is either x or y
                if curr.val == x:
                    x_found = True
                if curr.val == y:
                    y_found = True
                
                # Check if the current node's children are x and y (or vice versa)
                if curr.left != None and curr.right != None:
                    if curr.left.val == x and curr.right.val == y:
                        return False
                    if curr.left.val == y and curr.right.val == x:
                        return False
                
                # Add the children of the current node to the queue
                if curr.left != None:
                    q.put(curr.left)
                if curr.right != None:
                    q.put(curr.right)
            
            # After traversing one level, check if both x and y are found
            if x_found == True and y_found == True:
                return True
            # If only one is found, they are not cousins
            if x_found == True or y_found == True:
                return False
        
        return False

