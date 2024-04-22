def tandemBicycle(redShirtsSpeeds, blueShirtSpeeds, fastest):
    redShirtsSpeeds.sort()
    blueShirtSpeeds.sort()
    
    totalSpeed = 0
    
    if not fastest:
        reverseArrayinPlace(redShirtsSpeeds)
        
    for i in range(len(redShirtsSpeeds)):
        rider1 = redShirtsSpeeds[i]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - i - 1]
        
        totalSpeed += max(rider1, rider2)
        
    return totalSpeed

def reverseArrayinPlace(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], start[start]
        start += 1
        end -= 1
        
print(tandemBicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True))