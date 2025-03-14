#Code used for testing NLP concepts.

import unidecode 
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nlp = spacy.load('en_core_web_lg')

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def identify_topics(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    words = [word for word in tokens if word.lower() not in stop_words and word.isalpha()]
    count = Counter(words)
    topics = [item[0] for item in count.most_common(5)]
    return topics

def generate_output(text):
    topics = identify_topics(text)
    result = text
    result += '\nTopics: '
    for topic in topics:
        result += f'\n- {topic}'
    return result

file_name = input("Enter the file name: ") + '.txt'
text = read_file(file_name)
final_text = generate_output(text)

print(final_text)


