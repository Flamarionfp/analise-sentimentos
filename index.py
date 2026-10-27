from tractive import removeWordsOfStopWords, bagOfWords
from resolveSentense import countNegativeWords, countPositiveWords

testRewviews = [
   "O filme foi maravilhoso e os atores excelentes!", 
   "O roteiro foi fraco e o filme muito chato",  
   "O filme foi bom, mas o final foi decepcionante", 
   "A história é interessante"
]

positiveWords = [
  'bom',
  'boa', 
  'excelente', 
  'excelentes', 
  'maravilhoso',
  'ótimo', 'ótima',
  'divertido',
  'incrível'
]

negativeWords = [
  'ruim', 
  'péssimo', 
  'péssima', 
  'horrível',
  'chato',
  'terrível', 
  'fraco',
  'decepcionante'
]

stopwords = ['o', 'a', 'os', 'as', 'e', 'de', 'do', 'da', 'foi']
  
def contagemPorArray(reviews):
    for review in reviews:
        reviewWithoutStopWrds = removeWordsOfStopWords(review, stopwords)
        qtyPositiveWords = countPositiveWords(bagOfWords(reviewWithoutStopWrds), positiveWords)
        qtyNegativeWords = countNegativeWords(bagOfWords(reviewWithoutStopWrds), negativeWords)

        status = '??'
        if (qtyNegativeWords == qtyPositiveWords):
            status =  'EM CIMA DO MURO'
        elif (qtyNegativeWords > qtyPositiveWords):
            status =  'NEGATIVO'
        else:
            status = 'POSITIVO'
        print(f"Frase: {review}")
        print(f"Palavras positivas: {qtyPositiveWords}\nPalavras negativas: {qtyNegativeWords}\nResultado: {status}\n")

contagemPorArray(testRewviews)