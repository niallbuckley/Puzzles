# Python program to for tree traversals
 
# A class that represents an individual node in a
# Binary Tree
 
 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
# A function to do inorder tree traversal
def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.val)
 
        # now recur on right child
        printInorder(root.right)
 
 
# A function to do postorder tree traversal
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        print(root.val)


def subsets(nums):
    def dfs(n):
        print(n)
        if n >= len(nums):
            res.append(subset.copy())
            return

        # condition where it is increasing by one.
        subset.append(nums[n])
        dfs(n + 1)

        # condition where it is just returning an empty string
        subset.pop()
        dfs(n + 1)

    res = []
    subset = []
    dfs(0)
    return res

def permute(nums):

        def dfs(subset, visited, result):
            if len(subset) == len(nums):
                result.append(subset.copy())

            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    dfs(subset + [nums[i]], visited, result)
                    visited.remove(nums[i])

        result = []
        subset = []
        dfs(subset, set(), result)
        return result


def combinationSum(nums, target):

    def dfs(subset, result,index):
        print(subset)
        if sum(subset) == target:
            result.append(subset.copy())

        elif sum(subset) > target:
            #dfs(i+1)
            return

        for i in range(index, len(nums)):
            dfs(subset + [nums[i]], result, i)

    result = []
    subset = []
    dfs(subset, result, 0)
    return result

# A function to do preorder tree traversal
def printPreorder(root):
 
    if root:
 
        # First print the data of node
        print(root.val)
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)

def isBalanced(root):
    # Dont get!!
    if root:
        print (root.val)
        isBalanced(root.left)
        print (root.val)


def height(root):
    # Check if the binary tree is empty
    if root is None:
        # If TRUE return 0
        return 0

    # Recursively call height of each node
    print ('hi')
    leftAns = height(root.left)
    rightAns = height(root.right)

    print (leftAns, rightAns)
    return max(leftAns, rightAns) + 1

def isBalanced(root):

    def dfs(root):
        if not root: return [True, 0]

        left, right = dfs(root.left), dfs(root.right)
        balanced = (left[0] and right[0] and abs(left[1] - right[1] <= 1))

        return [balanced, 1+max(left[1],right[1])]

    p = dfs(root)
    return p[0]

def hasPathSum1(root):
    if not root:
        return 0
#    if not root.left and not root.right and :

#    return hasPathSum1(root.left) + root.val
    return hasPathSum1(root.right) + root.val

def huh(root,targetSum):
    ans = hasPathSum1(root)
    if ans == targetSum:
        return True
    return False

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    def helper(l,r):
        if l > r:
            return None
        mid = (l+r) // 2
        root = TreeNode(nums[mid])
        root.left = helper (l, mid-1)
        root.right = helper (mid+1, r)
        return root
    return helper(0,len(nums)-1)





def hasPathSum(root, targetSum):
    if not root:
        return 0
    return hasPathSum(root.left, targetSum) + root.val
    return hasPathSum(root.right, targetSum) + root.val
    #return hasPathSum(root.right, targetSum) + root.val
    #if targetSum == p:
    #    return True



    #sum += root.val
    #print (sum)
    #targetSum = targetSum - root.val
    #hasPathSum(root.right, targetSum)
    #targetSum = targetSum - root.val

    #return (targetSum == 0)

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)


#print ("Preorder traversal of binary tree is")
#printPreorder(root)
 
#print ("\nInorder traversal of binary tree is")
#printInorder(root)
 
#print ("\nPostorder traversal of binary tree is")
#printPostorder(root)
#print ("============")
#isBalanced(root)

#print (subsets('123'))

#print ( permute([1,2,3]) )

print (combinationSum( [2,3,6,7], 7))
#print ("Height: " + str(height(root)))


#print (isBalanced(root))

#print (hasPathSum(root,5))
#print (huh(root,7))

#print (hasPathSum1(root))

#sortedArrayToBST([-10,-3,0,5,9])