class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root, path):
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:
                self.array += [path]
            path += "->"
            helper(root.left,path)
            helper(root.right,path)
            
        
        self.array = []
        helper(root, "")
        return self.array
