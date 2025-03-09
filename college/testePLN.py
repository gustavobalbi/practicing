import unidecode 
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter


nlp = spacy.load('pt_core_news_lg')

def entrada(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as texto:
        conteudo = texto.read()
    return conteudo


def identificar_topicos(texto):
    stop_words = set(stopwords.words('portuguese'))
    tokens = word_tokenize(texto)
    palavras = [palavra for palavra in tokens if palavra.lower() not in stop_words and palavra.isalpha()]
    count = Counter(palavras)
    topicos = []
    for item in count.most_common(5):
        topicos.append(item[0])
    return topicos

def saida(texto):
    topicos = identificar_topicos(texto)
    resultado = texto

    resultado += '\nTópicos: '
    for topico in topicos:
        resultado += f'\n- {topico}'
    
    return resultado


nome_arquivo = input("Insira o nome do arquivo. ") + '.txt'
texto = entrada(nome_arquivo)
texto_final = saida(texto)

print(texto_final)


