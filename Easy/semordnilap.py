def semordnilap(words):
    #divide the string into set
    wordsSet = set(words)
    semordnilapPairs = []

    for word in words:
        reverse = word[::-1]

        if reverse in wordsSet and reverse != word:
            semordnilapPairs.append([word, reverse])
            wordsSet.remove(word)
            wordsSet.remove(reverse)
    
    print(semordnilapPairs)

    return semordnilapPairs

           
    
sampleInput = ["diaper", "abc", "test", "cba", "repaid"]        
semordnilap(sampleInput)