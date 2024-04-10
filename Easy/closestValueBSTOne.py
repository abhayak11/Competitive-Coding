def findClosestValueInBST(tree, target):
    return findClosestValueinBstHelper(tree, target, tree.value)

def findClosestValueinBstHelper(tree, target, closest):
    if tree is None:
        return closest
    
    if abs(tree.value - closest) < abs(tree.value - target):
        closest = tree.value
        
    if target < tree.value:
        return findClosestValueinBstHelper(tree, target, tree.right)
    
    if target > tree.value:
        return findClosestValueinBstHelper(tree, target, tree.left)
    
    else:
         return closest




class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

print(findClosestValueInBST( [
      {"id": "10", "left": "5", "right": "15", "value": 10},
      {"id": "15", "left": "13", "right": "22", "value": 15},
      {"id": "22", "left": null, "right": null, "value": 22},
      {"id": "13", "left": null, "right": "14", "value": 13},
      {"id": "14", "left": null, "right": null, "value": 14},
      {"id": "5", "left": "2", "right": "5-2", "value": 5},
      {"id": "5-2", "left": null, "right": null, "value": 5},
      {"id": "2", "left": "1", "right": null, "value": 2},
      {"id": "1", "left": null, "right": null, "value": 1}
    ], "10",  12))