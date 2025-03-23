#Code developed for splitting paragraphs based on their similarity and adding extracted topics. Is not prepared to handle exceptions.

import spacy
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords

# Load Portuguese language model
nlp = spacy.load("pt_core_news_lg")

def read_file(file_name):
    """Reads the file and returns its content."""
    with open(file_name, encoding="utf8") as file:
        content = file.read()
    return content

def tokenize_content(content):
    """Splits content into sentences."""
    sentences = sent_tokenize(content, language="portuguese")
    return sentences

def split_by_similarity(sentence_list, similarity_threshold=0.7):
    """Groups sentences into paragraphs based on similarity."""
    paragraphs = []
    current_paragraph = [sentence_list[0]]

    def preprocess(sentence):
        return " ".join([token.text for token in nlp(sentence) if not token.is_stop])

    for i in range(len(sentence_list) - 1):
        similarity = nlp(preprocess(sentence_list[i])).similarity(nlp(preprocess(sentence_list[i + 1])))

        if similarity > similarity_threshold:
            current_paragraph.append(sentence_list[i + 1])
        else:
            paragraphs.append(" ".join(current_paragraph))
            current_paragraph = [sentence_list[i + 1]]

    if current_paragraph:
        paragraphs.append(" ".join(current_paragraph))
    
    return paragraphs

def extract_topics(paragraphs):
    """Extracts key topics from paragraphs using named entities and frequent words."""
    paragraphs_with_topics = []
    stop_words = set(stopwords.words('portuguese'))

    for paragraph in paragraphs:
        doc = nlp(paragraph)
        entities = set([ent.text for ent in doc.ents])

        words = [
            token.lemma_ for token in doc 
            if token.is_alpha and token.text.lower() not in stop_words 
            and token.pos_ in {"NOUN", "ADJ"} 
        ]
        
        count = Counter(words)
        top_words = [item[0] for item in count.most_common(2)]
        combined_topics = list(set(entities).union(set(top_words)))
        formatted_topics = ", ".join(combined_topics)
        paragraph_with_topics = f"{paragraph}\n\nExtracted topics: {formatted_topics}"
        paragraphs_with_topics.append(paragraph_with_topics)

    return paragraphs_with_topics

print("""NLP EXTRACTOR INITIALIZED...
-------------------------------------------------------------- 
Enter the name of the file from which you want to extract data. 
Don't forget to include the file extension in your input.
""")

file_name = input("File name (name.extension): ")
original_content = read_file(file_name)
original_sentence_list = tokenize_content(original_content)
paragraphs = split_by_similarity(original_sentence_list)
final_text = extract_topics(paragraphs)

for paragraph in final_text:
    print(paragraph)
    print("\n" + "-"*50 + "\n")


