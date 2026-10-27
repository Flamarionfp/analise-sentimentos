
def countPositiveWords(obectOfCountedWords, positiveWords):
    positiveStatus = 0
    for positiveWord in  positiveWords:
        if (positiveWord in list(obectOfCountedWords.keys())):
            positiveStatus+=1
    return positiveStatus

def countNegativeWords(obectOfCountedWords, positiveWords):
    positiveStatus = 0
    for positiveWord in  positiveWords:
        if (positiveWord in list(obectOfCountedWords.keys())):
            positiveStatus+=1
    return positiveStatus