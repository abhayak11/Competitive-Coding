#time O(n)
#space O(n)
#only works for sorted array

def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallerIdx = 0
    largerIdx = len(array) - 1
    
    for i in reversed(range(len(array))):
        smaller = array[smallerIdx]
        larger = array[largerIdx]
        
        if abs(smaller) > abs(larger):
            sortedSquares[i] = smaller*smaller
            smallerIdx += 1
            
        else:
            sortedSquares[i] = larger*larger
            largerIdx -= 1
            
    return sortedSquares


print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))
        