import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import re
import pandas as pd

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

# Load and clean resume
with open("D:/NLP-Mini-Projects/resume_keyword_extractor/data/resume1.txt", 'r', encoding = 'utf-8') as file:
    resume_text = file.read()

resume_text = re.sub(r'\n+', ' ', resume_text)
resume_text = re.sub(r'[^\w\s]', '', resume_text)

#Run NLP pipeline
doc = nlp(resume_text)

#Extract keywords(noun, proper nouns) and remove stopwords
keywords = []
for token in doc:
    if token.text.lower() not in STOP_WORDS and not token.is_punct and token.pos_ in ["NOUN", "PROPN"]:
        keywords.append(token.text.lower())

# Remove duplicates
unique_keywords = list(set(keywords))

# Load predefined skills from CSV
skills_df = pd.read_csv("D:/NLP-Mini-Projects/resume_keyword_extractor/predefined_skills/skills.csv")
skill_list = skills_df["Skill"].str.lower().tolist()

#Filter extracted keywords against skill list
filtered_keywords = [kw for kw in unique_keywords if kw in skill_list]

print("Filtered Keywords foun in Resume:\n")
for word in filtered_keywords:
    print("-",word)

output_df = pd.DataFrame(filtered_keywords, columns=["Matched Skills"])
output_df.to_csv("D:/NLP-Mini-Projects/resume_keyword_extractor/output/spacy_output_keywords.csv")
print("\nExtracted skills saved to 'spacy_output_keywords.csv'")