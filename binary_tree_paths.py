class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        string = str(root.val) 
        string1 = Solution.helper(self, root.left, string)
        string2 = Solution.helper(self, root.right, string)
        if not string1 and not string2:
            return string
        if not string1:
            return [string2]
        if not string2:
            return [string1]
        return string1, string2 
        
    def helper(self,root,string):
        if not root:
            return None
        string += "->" + str(root.val)
        if root.left:
            return Solution.helper(self, root.left, string)
        if root.right:
            return Solution.helper(self, root.right, string)
        
        return string


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
