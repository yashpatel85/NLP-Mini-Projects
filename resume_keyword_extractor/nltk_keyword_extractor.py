import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag

import os

def load_resume(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as f:
        return f.read()
    
def extract_keywords(text):
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha() and word.lower() not in stop_words]

    tagged = pos_tag(tokens)
    keywords = [word for word, tag in tagged if tag in ["NN","NNP","JJ"]]

    return sorted(set(keywords), key=str.lower)

def save_keywords(keywords, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for word in keywords:
            f.write(word + "\n")

if __name__ == "__main__":
    resume_path = os.path.join("D:/NLP-Mini-Projects/resume_keyword_extractor/data/resume1.txt")
    output_path = os.path.join("D:/NLP-Mini-Projects/resume_keyword_extractor/output/extracted_keywords.txt")

    text = load_resume(resume_path)
    keywords = extract_keywords(text)
    save_keywords(keywords, output_path)

    print(f"Extracted {len(keywords)} keywords.")