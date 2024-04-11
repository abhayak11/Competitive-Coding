class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

def branchSums(root):
    sums = []
    intermediateSum(root, 0 sum)
    return sums

def intermediateSum(node, runningSum, sums):
    
    if node is None:
        return
    
    newRunningSum = runningSum + node.value
    
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        
    intermediateSum(node.left, newRunningSum, sums)
    intermediateSum(node.right, newRunningSum, sums)
    
    
    