# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        if (root == None):
            return []
        
        result = []
        curQ = [root]
        qCount = 0
        k = 1
        temp = []
        j = 0
        
        while(len(curQ)):
            node = curQ.pop(0)
            temp.append(node.val)
            qCount += 1
            
            if(node.left):
                curQ.append(node.left)
                j += 1
            if(node.right):
                curQ.append(node.right)
                j += 1
                    
            if(qCount == k):
                result.append(temp[-1])
                k = j
                j=0
                qCount = 0
                temp= []
                
        return result          
                
                
                
        