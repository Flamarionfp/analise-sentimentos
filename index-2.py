from tractive import removeWordsOfStopWords, bagOfWords
from resolveSentense import countNegativeWords, countPositiveWords

# Array atualizado com todas as frases das categorias solicitadas
testRewviews = [
    # Sentimentos claramente positivos
    "Achei a experiência maravilhosa!",
    "O atendimento foi excelente e muito atencioso.",
    "Fiquei muito feliz com o resultado final do projeto.",
    "A comida deste restaurante é deliciosa, recomendo a todos.",
    "O show foi espetacular, a melhor noite da minha vida!",
    
    # Sentimentos claramente negativos
    "Fiquei extremamente desapontado com a qualidade do produto.",
    "O serviço de entrega foi terrível e muito demorado.",
    "Achei o filme muito chato e sem graça.",
    "Estou frustrado com a falta de suporte técnico.",
    "O ambiente estava sujo e mal conservado, não volto mais.",
    
    # Frases neutras
    "O livro tem 300 páginas.",
    "A reunião está marcada para as 14h.",
    "O céu hoje está nublado.",
    "Comprei uma camisa azul na loja.",
    "O ônibus chegou no horário previsto.",
    
    # Negação
    "Não gostei do atendimento.",
    "Não recomendo este produto para ninguém.",
    "Não fiquei satisfeito com o resultado da pintura.",
    "Não achei a comida saborosa.",
    "Não consegui entender a explicação do professor.",
    
    # Contraste
    "O filme começou bem, mas terminou de forma decepcionante.",
    "A entrada estava deliciosa, porém o prato principal deixou a desejar.",
    "O hotel era bonito, contudo o serviço de quarto era péssimo.",
    "A ideia do projeto era boa, no entanto a execução falhou miseravelmente.",
    "A interface do aplicativo é amigável, mas ele trava constantemente.",
    
    # Palavra positiva que não representa sentimento positivo
    "O atendimento foi bom, mas o produto é péssimo.",
    "O design é bonito, pena que não funciona direito.",
    "A intenção foi ótima, mas o resultado foi um desastre.",
    "O início foi promissor, mas o final arruinou tudo.",
    "Até achei simpático, mas o serviço deixou muito a desejar."
]

# Expandimos o dicionário para cobrir os novos exemplos
positiveWords = [
  'bom', 'boa', 'excelente', 'excelentes', 'maravilhoso', 'maravilhosa',
  'ótimo', 'ótima', 'divertido', 'incrível', 'atencioso', 'feliz', 
  'deliciosa', 'espetacular', 'bem', 'bonito', 'amigável', 'promissor', 'simpático'
]

negativeWords = [
  'ruim', 'péssimo', 'péssima', 'horrível', 'chato', 'terrível', 'fraco',
  'decepcionante', 'desapontado', 'demorado', 'frustrado', 'sujo', 'desastre', 'arruinou'
]

stopwords = [
    'o', 'a', 'os', 'as', 'e', 'de', 'do', 'da', 'foi', 
    'com', 'um', 'uma', 'para', 'na', 'no', 'que', 'mas', 'porém'
]
  
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
        print("-" * 40)

contagemPorArray(testRewviews)