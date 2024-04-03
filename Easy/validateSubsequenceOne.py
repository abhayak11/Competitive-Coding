#time O(n) 
#space O(1)

def validateSubsequence(array, sequence):
    arrayIdx = 0
    sequenceIdx = 0 
    
    while arrayIdx < len(array) and sequenceIdx < len(sequence):
        if array[arrayIdx] == sequence[sequenceIdx]:
            sequenceIdx += 1
        
        arrayIdx += 1
        
    if len(sequence) == sequenceIdx:
        return True
    
    else:
        return False
    
    
    
print(validateSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))