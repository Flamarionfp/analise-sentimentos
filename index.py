#reviews = [
#    "O filme foi maravilhoso e os atores excelentes!", 
#    "O roteiro foi fraco e o filme muito chato",  
#    "O filme foi bom, mas o final foi decepcionante", 
#    "A história é interessante"]
#   ]

REVIEW = "O filme foi maravilhoso e os atores excelentes!"

def removeSpecialCharacters(text):
    return "".join(c for c in text if c.isalnum() or c.isspace())


def sanitizeReview(review):
    reviewLower = review.lower()
    
    return removeSpecialCharacters(reviewLower)


def tokenizeReview(review):
    return sanitizeReview(review).split()


stopwords = ['o', 'a', 'os', 'as', 'e', 'de', 'do', 'da', 'foi']
    
def removeWordsOfStopWords(reviewArray, stopwords):
    return
    
reviewWithoutStopWrds = removeWordsOfStopWords(tokenizeReview(REVIEW), stopwords)



def bagOfWords(words):
    criticas = [
        ['filme', 'bom', 'excelente'],
        ['filme', 'ruim', 'chato'],
        ['filme', 'bom', 'divertido']
    ]
    contagem = {palavra:0 for palavra in words}

    for sublista in criticas:
        for palavra in sublista:
            if palavra in contagem:
                contagem[palavra]+=1;
    return contagem;
        
