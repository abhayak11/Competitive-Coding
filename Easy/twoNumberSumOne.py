def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            
            numberOne = array[i]
            numberTwo = array[j]
            
            currentSum = numberOne + numberTwo
            
            if currentSum == targetSum:
                return [numberOne, numberTwo]
                

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))