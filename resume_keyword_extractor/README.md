# 📝 Resume Keyword Extractor

This project is part of a 3-day NLP mini-project series designed to build foundational skills for real-world NLP applications.

## 🚀 Project Goal

Automatically extract relevant skill-based keywords from resume text using a predefined skill dictionary. This is helpful for recruiters, HR tech systems, or job portals to parse and understand candidate strengths.

---

## 📚 NLP Concepts Practiced

- Tokenization
- Stopword Removal
- POS (Part-of-Speech) Tagging
- Lemmatization
- Regex Matching

---

## 🛠️ Tools & Libraries

- `spaCy`: For advanced NLP preprocessing and POS tagging.
- `pandas`: For handling structured data.
- `re`: For regex-based matching.
- `streamlit`: For building an interactive web UI.

---

## 📂 Project Structure

Resume_Keyword_Extractor/
├── skills.csv # Dictionary of allowed skill keywords
├── extractor.py # Core script to extract keywords from resume text
├── streamlit_app.py # Web app interface built using Streamlit
├── sample_resume.txt # (Optional) Sample resume input for testing
└── README.md # This file


## 🧪 How It Works

1. The user pastes resume text into the app.
2. The text is cleaned and processed using spaCy:
   - Lowercased, tokenized, lemmatized.
   - Non-alphabetic tokens, stopwords, and short words are removed.
3. The script matches keywords from the cleaned text against those in `skills.csv`.
4. The extracted skills are displayed to the user.
5. Optionally, the keywords are exported to JSON or CSV.

---

## 💻 How to Run Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt
