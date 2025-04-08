import re
import nltk
nltk.data.path.append("C:/Users/Rony/nltk_data")
import string
import wordcloud
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import urllib.request

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

files = {
    "Alice": "https://www.gutenberg.org/files/11/11-0.txt",
    "LookingGlass": "https://www.gutenberg.org/files/12/12-0.txt",
    "Tangled": "https://www.gutenberg.org/files/13643/13643-0.txt"
}

def clean_book(text):
    start_pattern = r"\*\*\* START OF THIS PROJECT GUTENBERG EBOOK.*?\*\*\*"
    end_pattern = r"\*\*\* END OF THIS PROJECT GUTENBERG EBOOK.*?\*\*\*"
    text = re.split(start_pattern, text, flags=re.IGNORECASE)[-1]
    text = re.split(end_pattern, text, flags=re.IGNORECASE)[0]
    return text.strip()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = nltk.word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(tokens)

raw_books = {
    name: clean_book(urllib.request.urlopen(url).read().decode("utf-8"))
    for name, url in files.items()
}

cleaned_books = {name: preprocess_text(text) for name, text in raw_books.items()}

for name, text in cleaned_books.items():
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"Word Cloud - {name}")
    plt.show()

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(cleaned_books.values())
words = vectorizer.get_feature_names_out()
df = pd.DataFrame(X.T.toarray(), index=words, columns=cleaned_books.keys())

top_words = {}
for col in df.columns:
    top = df[col].sort_values(ascending=False).head(5)
    top_words[col] = top

for book, data in top_words.items():
    plt.figure(figsize=(6, 6))
    plt.pie(data, labels=data.index, autopct="%1.1f%%", startangle=140)
    plt.title(f"Top 5 TF-IDF Words - {book}")
    plt.show()
