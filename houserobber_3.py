class Binarytree:
    def __init__(self,value):
        self.value = value
        self.right_child = None
        self.left_child = None


    def insert_left(self,value):

        if self.left_child == None:
            self.left_child = Binarytree(value)
        
        else:
            new_node = Binarytree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self,value):

        if self.right_child == None:
            self.right_child = Binarytree(value)
        else:
            new_node = Binarytree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node
            
class Solution:
    def rob(self, root : Binarytree) -> int :
        def dfs(root):
            if not root:
                return [0,0]
            
            leftPair = dfs(root.left_child)
            rightPair = dfs(root.right_child)

            withroot = root.value + leftPair[1] +rightPair[1]
            withoutroot = max(leftPair) +max(rightPair)

            return [withroot,withoutroot]
        return max(dfs(root))



