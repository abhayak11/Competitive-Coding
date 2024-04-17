def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse = True)
    blueShirtHeights.sort(reverse = True)
    
    firstRowColor = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
   
    for i in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[i]
        blueShirtHeight = blueShirtHeights[i]
        if firstRowColor == "RED":
            if redShirtHeight >= blueShirtHeight:
                return False
            else:
                if blueShirtHeight >= redShirtHeight:
                    return True
               
               
    return True


print(classPhotos( [5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))