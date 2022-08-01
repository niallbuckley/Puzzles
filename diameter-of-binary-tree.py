class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        Solution.dfs(self,root)
        return self.diameter
            
    
    def dfs(self,root):
        if not root:
            return 0
        
        lHeight = Solution.dfs(self,root.left)
        rHeight = Solution.dfs(self,root.right)
        if lHeight + rHeight > self.diameter:
            self.diameter = lHeight + rHeight
        
        
        return max (lHeight, rHeight) + 1
        
