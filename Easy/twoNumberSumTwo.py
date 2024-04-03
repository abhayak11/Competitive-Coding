#O(n) time
#O(n) space


def twoNumberSum(array, targetSum):
    hashTableData = {}
    for firstNum in array:
        secondNum = targetSum - firstNum
    
        if secondNum in hashTableData:
            return [firstNum, secondNum]

        else:
            hashTableData[firstNum] = True
        

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))