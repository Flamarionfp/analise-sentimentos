def removeSpecialCharacters(text):
    return "".join(c for c in text if c.isalnum() or c.isspace())

def sanitizeReview(review):
    reviewLower = review.lower()
    
    return removeSpecialCharacters(reviewLower)

def tokenizeReview(review):
    return sanitizeReview(review).split()

def removeWordsOfStopWords(reviewArray, stopwords):
    changedArray = []
    for reviewWord in sanitizeReview(reviewArray).split():
        if (reviewWord not in stopwords):
            changedArray.append(reviewWord);
    return changedArray

def bagOfWords(words):
    contage = {palavra: 0 for palavra in words}
    keys = list(contage.keys())
    for word in words:
        if (word in keys):
            contage[word]+=1
    return contage;
