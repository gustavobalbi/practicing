import spacy

from nltk import sent_tokenize

nlp = spacy.load("pt_core_news_lg")

# funcao de abertura do arquivo
def read_archive(d_archive_name):
    with open(d_archive_name, encoding="utf8") as archive_content:
        content = archive_content.read()
    return content

# funcao que retira as stopwords e retorna o conteudo em formato de string/texto
def clear_content(d_initial_content):
    content = nlp(d_initial_content)
    cleared_content = ' '.join([token.text for token in content if not token.is_stop and token.text != ','])
    return cleared_content

# funcao que tokeniza o conteudo do texto por sentencas
def tokenize_content(d_cleared_content):
    sentences = sent_tokenize(d_cleared_content, language="portuguese")
    return sentences

# funcao que determina a similaridade entre as sentencas do texto
def semantic_similarity(d_list_sentences):
    bigrams = []
    for i in range(len(d_list_sentences)-1):
        bigrams.append({})
        calc_similarity = nlp(d_list_sentences[i]).similarity(nlp(d_list_sentences[i+1]))
        print("-------------------", i+1, "---------------------")
        print("Primeira sentença: ", d_list_sentences[i])
        print("Segunda sentença: ", d_list_sentences[i+1])
        print("Similaridade: ", calc_similarity)
        bigrams[i][f'Bigrama N°{i+1}'] = calc_similarity
    print(bigrams)
    return bigrams

def similars(bigrams):
    somatory = 0
    count = 0
    high_similarity = []

    index = 0
    for item in bigrams:
        somatory += float(item[f'Bigrama N°{index+1}'])
        count += 1
        index += 1

    avrg = somatory/count

    index = -1
    list_index = 0
    for item in bigrams:
        index += 1
        if float(item[f'Bigrama N°{index+1}']) > avrg:
            high_similarity.append(index+1)

    high_similarityDICT = {}
    print(avrg)
    high_similarityDICT['índice dos similares'] = high_similarity 
    print(high_similarityDICT)
def subtopics(similar_sentences):
    print()

# main program
print("""NLP EXTRACTOR INITIALIZED...
-------------------------------------------------------------- 
Insert the archive's name you want to obtain the data. 
Don't forget to add the archive's format in your input.
""")

initial_content = read_archive('mariele.txt')

content_cleared = clear_content(initial_content)

list_content = tokenize_content(content_cleared)

bigramas = semantic_similarity(list_content)

similars(bigramas)