#time O(nlogn) 
#space O(n)

def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    
    for i in range(len(array)):
        value = array[i]
        sortedSquares[i] = value * value
        
    sortedSquares.sort()
    return sortedSquares


print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))
        