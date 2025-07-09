import pdfplumber
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#  English language model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    """Extract all text from a PDF file."""
    with pdfplumber.open(file) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)

def clean_text(text):
    """Lemmatize, remove stopwords and non-alpha tokens."""
    doc = nlp(text)
    return [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]

def compute_similarity(resume_text, job_text):
    """Compare resume and job description using TF-IDF + cosine similarity."""
    resume_keywords = clean_text(resume_text)
    job_keywords = clean_text(job_text)

    vect = TfidfVectorizer()
    tfidf = vect.fit_transform([
        " ".join(resume_keywords),
        " ".join(job_keywords)
    ])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

    return score, resume_keywords, job_keywords
