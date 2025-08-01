import streamlit as st
import pandas as pd
import spacy
import re

nlp = spacy.load("en_core_web_sm")

@st.cache_data
def load_skills():
    df = pd.read_csv("D:/NLP-Mini-Projects/resume_keyword_extractor/predefined_skills/skills.csv")
    return set(df["Skill"].str.lower().str.strip())

skills_set = load_skills()

def extract_keywords(text):
    text = re.sub(r'[^\w\s]', '', text)
    doc = nlp(text.lower())

    keywords = set()
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN", "VERB"] and not token.is_stop:
            if token.text.strip() in skills_set:
                keywords.add(token.text.strip())
    return sorted(keywords)

# Streamlit UI
st.title("📄 Resume Skill Extractor")
st.write("Upload your resume (.txt) to extract matching skills.")

uploaded_file = st.file_uploader("Choose a text file", type="txt")

if uploaded_file is not None:
    file_text = uploaded_file.read().decode("utf-8")
    st.subheader("📄 Resume Preview:")
    st.code(file_text[:1000], language='text')  # Show first 1000 chars

    with st.spinner("Extracting skills..."):
        matched_skills = extract_keywords(file_text)

    st.success("✅ Skills extracted successfully!")
    st.subheader("🧠 Matched Skills from Resume:")
    if matched_skills:
        st.write(", ".join(matched_skills))
    else:
        st.warning("No matching skills found.")