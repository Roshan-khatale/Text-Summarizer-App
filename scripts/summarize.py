import nltk
nltk.download('punkt')

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
import numpy as np

def summarize(text, n=2):
    sentences = sent_tokenize(text)
    if len(sentences) <= n:
        return text
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)
    scores = np.array(X.sum(axis=1)).flatten()
    ranked = [sentences[i] for i in scores.argsort()[-n:][::-1]]
    return ' '.join(ranked)