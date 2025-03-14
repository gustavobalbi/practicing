import spacy
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords


nlp = spacy.load("pt_core_news_lg")

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, encoding="utf8") as arquivo:
        conteudo = arquivo.read()
    return conteudo

def limpar_conteudo(conteudo_inicial):
    conteudo = nlp(conteudo_inicial)  
    conteudo_limpo = ' '.join([token.text for token in conteudo if not token.is_stop and token.text != ','])
    return conteudo_limpo

def tokenizar_conteudo(conteudo):
    sentencas = sent_tokenize(conteudo, language="portuguese")
    return sentencas

def dividir_por_similaridade(lista_sentencas, limite_similaridade=0.7):
    paragrafos = []
    paragrafo_atual = [lista_sentencas[0]]

    for i in range(len(lista_sentencas) - 1):
        similaridade = nlp(lista_sentencas[i]).similarity(nlp(lista_sentencas[i + 1]))


        if similaridade > limite_similaridade:
            paragrafo_atual.append(lista_sentencas[i + 1])
        else:
            paragrafos.append(" ".join(paragrafo_atual))
            paragrafo_atual = [lista_sentencas[i + 1]]


    if paragrafo_atual:
        paragrafos.append(" ".join(paragrafo_atual))

    return paragrafos

def topicos(paragrafos):
    paragrafos_com_topicos = []
    stop_words = set(stopwords.words('portuguese'))

    for paragrafo in paragrafos:
        doc = nlp(paragrafo)
        entidades = set([ent.text for ent in doc.ents])

        tokens = word_tokenize(paragrafo)
        palavras = [palavra for palavra in tokens if palavra.lower() not in stop_words and palavra.isalpha()]
        
        count = Counter(palavras)
        topicos_palavras = [item[0] for item in count.most_common(3)]
        topicos_combinados = list(entidades) + topicos_palavras
        topicos_formatados = ", ".join(topicos_combinados)
        paragrafo_com_topicos = f"{paragrafo}\n\nTópicos extraídos: {topicos_formatados}"
        paragrafos_com_topicos.append(paragrafo_com_topicos)

    return paragrafos_com_topicos

        


print("""EXTRATOR DE NLP INICIALIZADO...
-------------------------------------------------------------- 
Insira o nome do arquivo do qual deseja extrair os dados. 
Não se esqueça de incluir a extensão do arquivo no seu input.
""")

nome_arquivo = input("Nome do arquivo (nome.extensão): ")
conteudo_original = ler_arquivo(nome_arquivo)
conteudo_limpo = limpar_conteudo(conteudo_original)
lista_sentencas_limpo = tokenizar_conteudo(conteudo_limpo)
lista_sentencas_original = tokenizar_conteudo(conteudo_original)
paragrafos = dividir_por_similaridade(lista_sentencas_original)
texto_final = topicos(paragrafos)

for paragrafo in texto_final:
    print(paragrafo)
    print("\n" + "-"*50 + "\n")
