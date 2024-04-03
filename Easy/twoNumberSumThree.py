#time O(nlogn)
#space O(1)

def twoNumberSum(array, targetSum):
    array.sort()
    min = 0
    max = len(array) - 1
    
    while min < max:
        currentSum = array[min] + array[max]
        
        if currentSum == targetSum:
            return[array[min], array[max]]
        
        elif currentSum < targetSum:
            min = min + 1
        
        elif currentSum > targetSum:
            max = max - 1
        
    return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
